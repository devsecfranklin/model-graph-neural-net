variable "gcp_region" {
  description = "The region will be used to choose the default location for regional resources. Regional resources are spread across several zones."
  type        = string
}

variable "gcp_zone" {
  description = "The zone will be used to choose the default location for zonal resources. Zonal resources exist in a single zone."
}

variable "gcp_project_id" {
  description = "The project indicates the default GCP project ID"
  type        = string
}

variable "name" {
  description = "Name to add to our resources"
  type        = string
}

variable "aws_bucket" {
  type    = string
  default = "backend-datastore"
}

variable "gcp_bucket" {
  type    = string
  default = "backend-datastore"
}
