output "dag_bucket" {
  value = aws_s3_bucket.dag_bucket.bucket
}

output "log_bucket" {
  value = aws_s3_bucket.log_bucket.bucket
}
