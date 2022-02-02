aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin {{cookiecutter.aws_id}}.dkr.ecr.eu-central-1.amazonaws.com

docker build -t dev:latest -f compose/lambda_extended/Dockerfile .
docker tag dev:latest {{cookiecutter.aws_id}}.dkr.ecr.eu-central-1.amazonaws.com/dev_lambda_extended:latest
docker push {{cookiecutter.aws_id}}.dkr.ecr.eu-central-1.amazonaws.com/dev_lambda_extended:latest

docker build -t dev:latest -f compose/lambda_base/Dockerfile .
docker tag dev:latest {{cookiecutter.aws_id}}.dkr.ecr.eu-central-1.amazonaws.com/dev_lambda_base:latest
docker push {{cookiecutter.aws_id}}.dkr.ecr.eu-central-1.amazonaws.com/dev_lambda_base:latest

cd serverless_config && serverless deploy --stage dev
