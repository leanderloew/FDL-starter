# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/base-notebook:python-3.9.7
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    vim-tiny \
    git \
    inkscape \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    # ---- nbconvert dependencies ----
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
    # ----
    tzdata \
    unzip \
    nano-tiny \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create alternative for nano -> nano-tiny
RUN update-alternatives --install /usr/bin/nano nano /bin/nano-tiny 10
RUN conda install -c anaconda psycopg2
RUN pip install matplotlib

RUN apt-get update && apt-get install -y gnupg2
RUN apt-get install -y curl

COPY ./requirements/base.txt .
RUN pip --no-cache-dir install -r base.txt

COPY ./requirements/local.txt .
RUN pip --no-cache-dir install -r local.txt

COPY ./compose/jupyter_notebook/jupyter_server_config.py /etc/jupyter/
COPY ./compose/jupyter_notebook/overrides.json /opt/conda/share/jupyter/lab/settings/

# set display port to avoid crash
ENV DISPLAY=:99

ENV PYTHONPATH=/app

WORKDIR /app
# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID


