terraform {
  required_providers {
    //null     = "~> 3.1.0"
    random   = "~> 3.3.0"
    external = "~> 2.2.0"
    aws = {
      source = "hashicorp/aws"
    }
  }
  backend "gcs" {
    bucket = "pso-automation-dev"
    prefix = "gnn-test"
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
  //impersonate_service_account = var.service_account_terraform
}

provider "google-beta" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

provider "aws" {
  profile = "default"
  region  = "us-east-2"
}
