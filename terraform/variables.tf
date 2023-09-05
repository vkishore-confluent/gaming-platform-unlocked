variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key (also referred as Cloud API ID)"
  type        = string
  default = "6IJ73MQCZ7T522RV"
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret"
  type        = string
  sensitive   = true
  default = "iovS6OeT2286jkoCYGH55zeMvc0glpnnfs6SUJh83o09I66Y4ZkTmaPjQU9Xhj8N"
}