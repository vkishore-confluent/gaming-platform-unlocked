output client_api_key {
  value = confluent_api_key.tf_cluster_admin_apikey.id
}

# output client_api_secret {
#   value = confluent_api_key.tf_cluster_admin_apikey.secret
# }