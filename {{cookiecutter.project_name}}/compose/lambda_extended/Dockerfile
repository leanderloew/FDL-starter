FROM public.ecr.aws/lambda/python:3.9

RUN pip install --upgrade pip

RUN pip install psycopg2-binary

#setting workdir this way so we coppy all relevant files to it
WORKDIR ${LAMBDA_TASK_ROOT}

COPY ./requirements/base.txt .
RUN pip --no-cache-dir install -r base.txt

COPY ./requirements/extended.txt .
RUN pip --no-cache-dir install -r extended.txt

ADD app .

#this should jsut rerun every time, put this before if you dont want to reinstall the apps
RUN mkdir /root/.ssh/
ADD .ssh/id_rsa /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
COPY ./requirements/private_libraries.txt .
RUN pip --no-cache-dir install -r private_libraries.txt
RUN rm /root/.ssh/id_rsa

CMD [ "main.handler" ]
