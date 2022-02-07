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

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
#RUN echo "deb [arch=armhf] http://10.10.12.14/raspbian/ bullseye main contrib non-free rpi" > /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list
COPY trusted.gpg /etc/apt/trusted.gpg
COPY resolv.conf /etc/resolv.conf

RUN \
    
    apt-get update; \
    apt-get install -y make libgraphviz-dev python3-scipy libopenblas-base libatlas3-base; \
    python -m pip install --upgrade pip; \
    python -m pip install -r /workspace/cluster/requirements.txt 

CMD ["python", "/workspace/src/train.py" ] 

