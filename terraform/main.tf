# #This part creates environment
# resource "confluent_environment" "development" {
#   display_name = "Development"
#   lifecycle {
#     prevent_destroy = true
#   }
# }

#This part creates cluster inside environment
resource "confluent_kafka_cluster" "basic" {
  display_name = "Gaming Platform Unlocked"
  availability = "SINGLE_ZONE"
  cloud        = "AWS"
  region       = "us-east-2"
  basic {}

  environment {
    id = "env-97ryr0" #change to confluent_environment.development.id
  }

  lifecycle {
    prevent_destroy = true
  }
}

##This part creates service account
resource "confluent_service_account" "tf_cluster_admin" {
  display_name = "tf_cluster_admin"
  description  = "terraform cluster admin service account"
}

##This part assigned role to the user  account created
resource "confluent_role_binding" "tf_cluster_admin-kafka-cluster-admin" {
  principal   = "User:${confluent_service_account.tf_cluster_admin.id}"
  role_name   = "CloudClusterAdmin"
  crn_pattern = confluent_kafka_cluster.basic.rbac_crn
}

# This part creates API Key for service account
resource "confluent_api_key" "tf_cluster_admin_apikey" {
  display_name = "tf_cluster_admin_apikey"
  description  = "Kafka API Key that is owned by 'tf_cluster_admin' service account"
  owner {
    id          = confluent_service_account.tf_cluster_admin.id
    api_version = confluent_service_account.tf_cluster_admin.api_version
    kind        = confluent_service_account.tf_cluster_admin.kind
    }
  managed_resource {
    id          = confluent_kafka_cluster.basic.id
    api_version = confluent_kafka_cluster.basic.api_version
    kind        = confluent_kafka_cluster.basic.kind
    environment {
      id = "env-97ryr0" #change to confluent_environment.development.id
    }
  }
}

# This part creates a topic 
resource "confluent_kafka_topic" "game_transactions" {
  kafka_cluster {
    id = confluent_kafka_cluster.basic.id
  }
  topic_name    = "game_transactions"
  rest_endpoint = confluent_kafka_cluster.basic.rest_endpoint
  credentials {
    key    = confluent_api_key.tf_cluster_admin_apikey.id
    secret = confluent_api_key.tf_cluster_admin_apikey.secret
  }
}

resource "confluent_kafka_topic" "txn_raw" {
  kafka_cluster {
    id = confluent_kafka_cluster.basic.id
  }
  topic_name    = "txn_raw"
  rest_endpoint = confluent_kafka_cluster.basic.rest_endpoint
  credentials {
    key    = confluent_api_key.tf_cluster_admin_apikey.id
    secret = confluent_api_key.tf_cluster_admin_apikey.secret
  }
}