# FDL-starter
Using this template you can have a scalable, automated and cheap api server running in 10 minutes! Based on FastApi, Docker and Lambdas (FDL).

## Overview / Features
This is my very opinionated starter template for fastapi based projects. It includes a lot of my
learned best practices, it is the template I personally use. it includes: 

1. Fastapi as an api framework 
2. Local API Server and a Jupyter server, using docker-compose
3. A dev and a production environment, seperated by .envs files 
   1. so you can easily switch locally by selecting a different docker compose-file
4. Infra using Serverless and AWS Lambda
5. Deployment using docker .sh files and AWS ECR 

## Setup 
### Pre-Requisites
1. this only works for linux (because of the .sh files we use)
   1. it should be straight forward to extend to MAC / Windows, pull requests are welcome
2. python + cookiecutter has to be installed
3. npm has to be installed locally to set up serverless framework
4. additionally you need: 
   1. an aws account
   2. a serverless account
   3. (optional) a postgres database accessible by the Lambda functions (preferably in the same VPN)
   4. (optional but recommended) a sentry account
### Initial Set up
1. go to serverless and create an organization /  app 
   1. it has to be the same name as the serverless_org and the serverless_app parameters
2. run the cookiecutter for example by:
```
    cookiecutter git@github.com:leanderloew/FPL-starter.git
```
3. follow the command line to set up your input
4. wait for the project to be generated

5. now you have to set up the Elastic Container Registries, you can do that by running 
```
    cd terraform/ecr
    terraform init
    terraform plan
    terraform apply
    cd ../..
```
6. (Optional!) you can optionally run similar code to create the production and development databases, however please make sure
   the code doesn't destroy existing databases, also if in doubt create the databases using an online interface instead
7. next you have to set up serverless framework run: 
```
   cd serverless_config
   npm i serverless
   cd ../
```
8. finally you can run your first development deploy
```
   bash deploy_dev.sh
```
10. you can follow one of the health urls you should see in your browser:
```
   {"status":200}
```
11. to run the local api server and jupyter server simply run 
```
docker-compost -f local_dev.yml up 
```
12. you can run a local production server instead with 
```
docker-compost -f local_prod.yml up 
```

### Re-Deployment
when you have a new change you want to deploy to development run 
```
   bash deploy_dev.sh
```
similarly when you want to deploy to production run 
```
   bash deploy_prod.sh
```
### Costs
1. if you set it up without database the costs should be basically 0, also a lot of requests (1 million) and 400.000 gbseconds will be covered by aws free tier. 
2. however, if you set up the hosted database it will always cost you some amount.
### Additional recommended setup
1. you can integrate the deployment script into a remote deployment for example with github actions
   1. the main pain will then be to handle the environment variables
2. it is recommended not to push before setting up and running some tests
### Disclaimer
running this code has the potential to: 
1. destroy existing databases
   1. only if you run the dev_db and prod_db terraform scripts
2. generate a lot of costs, if you receive a lot of requests somehow
you are yourself liable to make sure your project is secure and the costs stay in your budget. This setup is purely educational.

### TODO
## Additional Guides
1. Data Base Setup 
   1. Public AWS
   2. Private AWS with VPN
2. A demo app integrated with Retool
3. Pycharm + Docker compose setup for debugging
