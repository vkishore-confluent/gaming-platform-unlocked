variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key (also referred as Cloud API ID)"
  type        = string
  default = "TOJQJO536MKYCKC7"
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret"
  type        = string
  sensitive   = true
  default = "ELIEsPsQSGwQuw7/OXS3Ua09O2OtVbUMoHFsLYN3gS+Yz60CPecSx7dB7ewWd5su"
}