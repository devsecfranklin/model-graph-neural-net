resource "aws_s3_bucket" "s3_project_bucket" {
  bucket = var.aws_bucket

  versioning {
    enabled    = false
    mfa_delete = false
  }

  lifecycle {
    prevent_destroy = true
  }
}