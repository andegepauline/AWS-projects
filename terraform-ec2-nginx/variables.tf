# AWS region to deploy to
variable "aws_region" {
  default = "us-east-1"
}

# EC2 instance type
variable "instance_type" {
  default = "t2.micro"
}

# Amazon Linux 2 AMI ID for the selected region
variable "ami_id" {
  default = "ami-084a7d336e816906b"
}

# Allowed SSH IP address
variable "ssh_allowed_ip" {
  default = "105.160.85.176/32"
}
