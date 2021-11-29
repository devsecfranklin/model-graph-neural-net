# syntax=docker/dockerfile:1

FROM alpine:3.15

LABEL maintainer="Franklin <2730246+devsecfranklin@users.noreply.github.com>" \
      org.opencontainers.image.source="https://github.com/devsecfranklin/model-graph-neural-net"

WORKDIR /workspace
ENV MY_DIR /workspace
ADD . ${MY_DIR}

ENV MAIN_PKGS="\
        tini curl ca-certificates py3-numpy lapack \
        py3-numpy-f2py freetype jpeg libpng libstdc++ \
        libgomp graphviz-dev font-noto openssl gfortran make automake gcc g++ subversion python3-dev"

RUN set -ex; \
    apk update; \
    apk upgrade; \
    echo http://dl-cdn.alpinelinux.org/alpine/edge/main | tee /etc/apk/repositories; \
    echo http://dl-cdn.alpinelinux.org/alpine/edge/testing | tee -a /etc/apk/repositories; \
    echo http://dl-cdn.alpinelinux.org/alpine/edge/community | tee -a /etc/apk/repositories; \
    apk add --no-cache ${MAIN_PKGS}; \
    python3 -m ensurepip; \
    rm -r /usr/lib/python*/ensurepip; \
    pip3 --no-cache-dir install --upgrade pip setuptools wheel; \
    python3 -m pip install -r requirements.txt
   
