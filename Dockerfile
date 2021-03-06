# syntax=docker/dockerfile:1

FROM python:3.10.5-slim-bullseye

ARG BUILD_DATE
ARG USER="franklin"

LABEL maintainer="Franklin <2730246+devsecfranklin@users.noreply.github.com>" \
      org.opencontainers.image.source="https://github.com/devsecfranklin/model-graph-neural-net" \
      org.label-schema.build-date=$BUILD_DATE

WORKDIR /workspace
ENV MY_DIR /workspace/source

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
RUN pwd && ls ; \
    apt-get update; \
    apt-get install -y make gcc libgraphviz-dev && apt-get clean; \
    python -m pip install --upgrade pip; \
    python -m pip install -r ${MY_DIR}/gnn/training/requirements.txt

# need to access the data store somehow (local copy for now)
# The files are in a GCP storage bucket

CMD ["/usr/local/bin/python3", "${MY_DIR}/gnn/training/train.py" ]
