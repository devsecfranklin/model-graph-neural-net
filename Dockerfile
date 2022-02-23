# syntax=docker/dockerfile:1

FROM python:3.10.2-slim-bullseye

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
RUN \
    apt-get update; \
    apt-get install -y make gcc libgraphviz-dev  && apt-get clean; \
    python -m pip install --upgrade pip; \
    python -m pip install -r /workspace/gnn/training/requirements.txt 

# need to access the data store somehow (local copt for now)
# The files are in a GCP storage bucket

CMD ["/usr/local/bin/python3", "/workspace/gnn/training/train.py" ]
