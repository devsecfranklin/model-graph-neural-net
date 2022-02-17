# Cluster Build

Setup

```sh
sudo apt install libopenblas-base libatlas3-base
/mnt/clusterfs/google-cloud-sdk/bin/gcloud components update # no sudo needed
pip install -r cluster/requirements.txt
```

## Autotools Build

Find the Python3 binary automagically.

The Makefile.am file is processed by automake to create Makefile.in, which is in turn processed by configure to create Makefile, which is in turn used by make to build the software.

```sh
sudo apt install libtool autconf automake
make clean
libtoolize
aclocal
autoheader
autoreconf -i # or just autoconf
automake -a -c
./configure
config.status
cd cluster
make python
```

## Docker 

```sh
docker buildx create --name franklin
docker buildx use franklin
docker buildx build --platform linux/arm/v7 cluster/
docker buildx build --platform linux/arm/v7 -t franklin/gnn-collection:latest gnn/collection/
docker buildx build --platform linux_aarch64 -t franklin/gnn-training:latest gnn/training/
```
