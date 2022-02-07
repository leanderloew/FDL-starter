terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
  backend "remote" {
    organization = "{{cookiecutter.terraform_organization}}"
    workspaces {
      name = "{{cookiecutter.project_name}}_prod_db"
    }
  }
}

variable "DB_PW" {
}

variable "SUBNET_GRP" {
}

variable "SECURITY_GRP" {
}

provider "aws" {
  profile = "default"
  region  = "{{cookiecutter.aws_region}}"
}

# Use the latest production snapshot to create a dev instance.
resource "aws_db_instance" "prod" {
  allocated_storage    = 20
  max_allocated_storage = 100
  engine               = "postgres"
  instance_class       = "db.t2.micro"
  identifier = "{{cookiecutter.project_name}}_prod_db"
  name                 = "postgres"
  username             = "postgres"
  password             = var.DB_PW
  db_subnet_group_name = var.SUBNET_GRP
  apply_immediately = true
  publicly_accessible = true
  vpc_security_group_ids = [var.SECURITY_GRP]
  skip_final_snapshot = false
  snapshot_identifier = "{{cookiecutter.project_name}}_prod_db_snapshot"
  final_snapshot_identifier = "{{cookiecutter.project_name}}_prod_db_final_snapshot"

  lifecycle {
    ignore_changes = [snapshot_identifier]
  }
}