output bootstrap_servers {
  value = confluent_kafka_cluster.basic.bootstrap_endpoint
}

output client_api_key {
  value = confluent_api_key.tf_cluster_admin_apikey.id
}

output client_api_secret {
  value = confluent_api_key.tf_cluster_admin_apikey.secret
  sensitive = true
}