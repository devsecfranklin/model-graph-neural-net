# Cluster Build

Setup

```sh
sudo apt install libopenblas-base libatlas3-base
/mnt/clusterfs/google-cloud-sdk/bin/gcloud components update # no sudo needed
pip install -r cluster/requirements.txt
```

## Docker 

```sh
docker buildx create --name franklin
docker buildx use franklin
docker buildx build --platform linux/arm/v7 cluster/
docker buildx build --platform linux/arm/v7 -t franklin/gnn-collection:latest cluster/
```
