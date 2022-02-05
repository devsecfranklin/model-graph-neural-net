# syntax=docker/dockerfile:1

FROM python:3.10.2-bullseye

ARG BUILD_DATE
ARG USER="franklin"

LABEL maintainer="Franklin <2730246+devsecfranklin@users.noreply.github.com>" \
      org.opencontainers.image.source="https://github.com/devsecfranklin/model-graph-neural-net" \
      org.label-schema.build-date=$BUILD_DATE

WORKDIR /workspace
ENV MY_DIR /workspace
ADD ./* ${MY_DIR}/

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
RUN \
    apt-get update; \
    apt-get install -y make libgraphviz-dev; \
    ls -al; pwd ; \
    python -m pip install --upgrade pip; \
    python -m pip install -r ${MY_DIR}/src/requirements.txt 
    #/usr/local/bin/python /workspace/src/main.py

CMD ["python", "src/train.py" ] 
