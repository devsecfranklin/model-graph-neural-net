# syntax=docker/dockerfile:1

FROM python:3.10.2-bullseye

ARG BUILD_DATE
ARG USER="franklin"

LABEL maintainer="Franklin <2730246+devsecfranklin@users.noreply.github.com>" \
      org.opencontainers.image.source="https://github.com/devsecfranklin/model-graph-neural-net" \
      org.label-schema.build-date=$BUILD_DATE

WORKDIR /workspace
ENV MY_DIR /workspace
ADD . /workspace/

RUN cp /workspace/sources.list /etc/apt/sources.list # use our internal Debian mirror
COPY trusted.gpg /etc/apt/trusted.gpg
COPY resolv.conf /etc/resolv.conf
COPY requirements.txt /tmp/requirements.txt

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
RUN \
    apt-get update; \
    apt-get install -y make libgraphviz-dev
# Python time
RUN \
    python -m pip install --trusted-host storage1.lab.bitsmasher.net --no-index --find-links=http://storage1.lab.bitsmasher.net/pypi --upgrade pip; \
    python -m pip install --trusted-host storage1.lab.bitsmasher.net --no-index --find-links=http://storage1.lab.bitsmasher.net/pypi -r /tmp/requirements.txt 

CMD ["python", "/workspace/gnn/training/training.py" ] 

