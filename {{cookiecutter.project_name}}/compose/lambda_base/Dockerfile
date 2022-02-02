FROM public.ecr.aws/lambda/python:3.8

RUN pip install --upgrade pip

RUN pip install psycopg2-binary

#setting workdir this way so we coppy all relevant files to it
WORKDIR ${LAMBDA_TASK_ROOT}

# is needed to be able to import lightgbm :D
RUN yum -y install libgomp

COPY ./requirements/base.txt .
RUN pip --no-cache-dir install -r base.txt

ADD app .

CMD [ "main.handler" ]
