# syntax=docker/dockerfile:1

FROM python:3.10.4-bullseye

ARG BUILD_DATE
ARG USER="franklin"

LABEL maintainer="Franklin <2730246+devsecfranklin@users.noreply.github.com>" \
      org.opencontainers.image.source="https://github.com/devsecfranklin/model-graph-neural-net" \
      org.label-schema.build-date=$BUILD_DATE

WORKDIR /workspace
ENV MY_DIR /workspace
ADD . /workspace/

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
COPY sources.list /etc/apt/sources.list
COPY trusted.gpg /etc/apt/trusted.gpg
COPY resolv.conf /etc/resolv.conf
COPY requirements.txt /tmp/requirements.txt

RUN \
    apt-get update; \
    apt-get install -y make libgraphviz-dev; \
    python -m pip install --upgrade pip; \
    python -m pip install -r /tmp/requirements.txt 

CMD ["python", "/workspace/gnn/collection/collection.py" ] 

