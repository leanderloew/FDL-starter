# FPL-starter

## Overview / Features
This is my very opinionated starter template for fastapi based projects. It includes a lot of my
learned best practisces, it is the template I personally use. it includes: 

1. Fastapi as an api framework 
2. Local Server, including an API Server and a Jupyter server
3. A dev and a production environment, seperated by .envs files 
4. Deployment using Serverless and AWS Lambda
5. automated deployment using two .sh files and AWS ECR 
6. Local server, jupyter and deployment server all using seperate Docker containers
7. migration framework using Alembic 
8. a set of Sql Alchemy utils and boilerplate set up code
9. I used RDS as a postgres database but any postgres hoster would work

The goal is, with one click of a button to have a deployed, opinionated API server with database running. 
it covers important but often overlooked cases out of the box: 
1. different docker images as well as requirement files for different lambdas and environments
2. multiple .env files for local and remote as well as general
3. easy dev and prod switch, so you can easily apply changes to the prod environment from your PC
4. full integration with Pycharm (sadly you need the pro version)

## Setup 
1. cookiecutter has to be installed
2. you can invoke it using cookiecutter TODO add url 
3. additionally you need: 
   1. an aws account
   2. a postgres database accessible by the Lambda functions (preferably in the same VPN)
   3. a sentry account
   4. a serverless account

Here I have a full written guide and a here is a Youtube video about how you go from nothing to a running Database 
and Fastapi Server. 

there are additional guides about: 
1. writing api routes
2. setting up Lambda as well as the Database without VPN 
3. and here with VPN 
4. A demo app integrated with Retool (sponsored by them can be found here)
5. how I have set up Pycharm to use docker-compose
