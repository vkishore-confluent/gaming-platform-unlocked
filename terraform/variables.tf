variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key (also referred as Cloud API ID)"
  type        = string
  default = "WJZ2YA323XHB5DWQ"
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret"
  type        = string
  sensitive   = true
  default = "kZ7miPvZ41sop/wcWOwKT5mlQ65mGeQO6xTYCh+gvzKfYuUdoUrJYnjwPhFVLIcH"
}