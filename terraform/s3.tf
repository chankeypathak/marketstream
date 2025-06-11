resource "aws_s3_bucket" "dag_bucket" {
  bucket = "${var.project_name}-dag-bucket"
  force_destroy = true
}

resource "aws_s3_bucket" "log_bucket" {
  bucket = "${var.project_name}-log-bucket"
  force_destroy = true
}
