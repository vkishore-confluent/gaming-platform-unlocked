variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key (also referred as Cloud API ID)"
  type        = string
  default = "4PIOPFIO5ZAWBFAX"
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret"
  type        = string
  sensitive   = true
  default = "lzqLePKjuy9p0pKGHK+Ci4LUSqL1Fp9oAfCxSLWb/Bd86sH4cpXoULVCtaGDjNj0"
}
