# syntax=docker/dockerfile:1

FROM python:3.10.2-bullseye

ARG BUILD_DATE
ARG USER="franklin"

LABEL maintainer="Franklin <2730246+devsecfranklin@users.noreply.github.com>" \
      org.opencontainers.image.source="https://github.com/devsecfranklin/model-graph-neural-net" \
      org.label-schema.build-date=$BUILD_DATE

WORKDIR /workspace
ENV MY_DIR /workspace
ADD . ${MY_DIR}

##########################
# Get Terraform binaries #
##########################
# RUN for MYVER in 1.0.11; \
#    do \
#        wget --quiet https://releases.hashicorp.com/terraform/${MYVER}/terraform_${MYVER}_linux_amd64.zip -P /tmp; \
#            cd /tmp \
#          && unzip /tmp/terraform_${MYVER}_linux_amd64.zip \
#          && mv /tmp/terraform /usr/bin/terraform`echo ${MYVER}| cut -f2 -d'.'` \
#          && rm /tmp/terraform_${MYVER}_linux_amd64.zip \
#          && ln -s /usr/bin/terraform`echo ${MYVER}| cut -f2 -d'.'` /usr/bin/terraform; \
#    done

#####################
# Add some packages #
#####################
ENV DEBIAN_FRONTEND noninteractive
RUN \
    apt-get update; \
    apt-get install -y debconf apt-utils; \
    apt-get install -y make automake autoconf graphviz libgraphviz-dev; \
    /usr/local/bin/python -m pip install --upgrade pip; \
    pip install -r requirements.txt 
    #/usr/local/bin/python /workspace/src/main.py

# CMD ["python", "src/main.py" ] 
