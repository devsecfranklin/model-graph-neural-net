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

COPY sources.list /etc/apt/sources.list 
COPY trusted.gpg /etc/apt/trusted.gpg
COPY resolv.conf /etc/resolv.conf
COPY requirements.txt /tmp/requirements.txt

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
RUN \
    apt-get update; \
    apt-get install -y apt-utils; \
    apt-get install -y make libgraphviz-dev

RUN \
    python -m pip install --upgrade pip; \
    python -m pip install --trusted-host storage1.lab.bitsmasher.net --no-index --find-links=http://storage1.lab.bitsmasher.net/pypi -r /tmp/requirements.txt; \
    python -m pip install -U -i  https://pypi.org/simple psutil

CMD ["python", "/workspace/gnn/training/training.py" ] 

