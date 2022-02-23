# Build a Container to run in GKE

## Local Testing

- Use `make build` to create a local container image.
  - run the training script inside the container to verify

## Send Through CI

```sh
gcloud container images list
gcloud container images list-tags gcr.io/gcp-gcs-pso/model-graph-neural-net
```
