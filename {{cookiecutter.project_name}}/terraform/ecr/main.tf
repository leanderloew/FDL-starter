terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}
provider "aws" {
  profile = "default"
  region  = "{{cookiecutter.aws_region}}"
}
resource "aws_ecr_repository" "dev_ext" {
  name                 = "dev_{{cookiecutter.project_name}}_lambda_extended"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}
resource "aws_ecr_repository" "dev_base" {
  name                 = "dev_{{cookiecutter.project_name}}_lambda_base"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}
resource "aws_ecr_repository" "prod_ext" {
  name                 = "prod_{{cookiecutter.project_name}}_lambda_extended"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}
resource "aws_ecr_repository" "prod_base" {
  name                 = "prod_{{cookiecutter.project_name}}_lambda_base"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}


