resource "aws_iam_role" "mwaa_execution_role" {
  name = "${var.project_name}-mwaa-exec-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "airflow.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_mwaa_environment" "mwaa" {
  name              = "${var.project_name}-mwaa-env"
  airflow_version   = "2.9.0"
  environment_class = "mw1.small"
  dag_s3_path       = "dags"
  source_bucket_arn = aws_s3_bucket.dag_bucket.arn
  execution_role_arn = aws_iam_role.mwaa_execution_role.arn

  logging_configuration {
    dag_processing_logs { enabled = true log_level = "INFO" }
    scheduler_logs      { enabled = true log_level = "INFO" }
    task_logs           { enabled = true log_level = "INFO" }
    webserver_logs      { enabled = true log_level = "INFO" }
    worker_logs         { enabled = true log_level = "INFO" }
  }

  network_configuration {
    security_group_ids = []  # Add your VPC security group IDs
    subnet_ids         = []  # Add your subnet IDs
  }
}
