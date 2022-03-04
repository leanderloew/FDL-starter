FROM public.ecr.aws/lambda/python:3.9

RUN pip install --upgrade pip

RUN pip install psycopg2-binary

#setting workdir this way so we coppy all relevant files to it
WORKDIR ${LAMBDA_TASK_ROOT}
RUN yum -y install openssh-clients
RUN yum -y install git
# is needed to be able to import lightgbm :D
RUN yum -y install libgomp

COPY ./requirements/base.txt .
RUN pip --no-cache-dir install -r base.txt

COPY ./requirements/extended.txt .
RUN pip --no-cache-dir install -r extended.txt

COPY ./private_packages /private_packages
WORKDIR /private_packages
RUN bash install_packages.sh
WORKDIR /app

ADD app .

CMD [ "main.handler" ]
