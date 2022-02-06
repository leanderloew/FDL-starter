#this allready runs the main app etc.
#if we would want to rename the app we would have to modify that image
FROM python:3.9
#FROM public.ecr.aws/lambda/python:3.7
RUN pip install psycopg2-binary
USER root
WORKDIR /app

ENV PYTHONPATH=/app

COPY ./requirements/base.txt .
RUN pip --no-cache-dir install -r base.txt

COPY ./requirements/local.txt .
RUN pip --no-cache-dir install -r local.txt

#this is used to avoid writing files as some weired user
ARG UNAME=testuser
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

COPY ./app /app

RUN mkdir /root/.ssh/
ADD .ssh/id_rsa /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

COPY ./requirements/private_libraries.txt .
RUN pip --no-cache-dir install -r private_libraries.txt

RUN rm /root/.ssh/id_rsa

USER $UNAME
CMD /bin/bash