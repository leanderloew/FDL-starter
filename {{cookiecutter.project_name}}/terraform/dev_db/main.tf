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
      name = "{{cookiecutter.project_slug}}_dev_db"
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

data "aws_db_snapshot" "latest_prod_snapshot" {
  db_instance_identifier = "{{cookiecutter.project_slug}}_prod_db"
  most_recent            = true
}

# Use the latest production snapshot to create a dev instance.
resource "aws_db_instance" "dev" {

  allocated_storage    = 100
  max_allocated_storage = 200
  engine               = "postgres"
  instance_class       = "db.t2.micro"
  identifier = "{{cookiecutter.project_slug}}_dev_db"
  name                 = "postgres"
  username             = "postgres"
  password             = var.DB_PW
  db_subnet_group_name = var.SUBNET_GRP
  apply_immediately = true
  publicly_accessible = true
  vpc_security_group_ids = [var.SECURITY_GRP]
  skip_final_snapshot = true
  snapshot_identifier = data.aws_db_snapshot.latest_prod_snapshot.id
  lifecycle {
    ignore_changes = [snapshot_identifier]
  }
}
