# Manage Storage Key

## Setup


```sh
# doas apk update && doas apk add pass # install pass on alpine
gpg --list-keys # get your public key id
pass init C25565E4701F4ED36A0711AA114F3606EFD923BB # id of your public GPG key
```

## Store credentials in "pass" manager.


```sh
pass insert franklin-storage-key.json
pass ls
pass show franklin-storage-key.json
```

```sh
dvc remote add -d data gs://backend-dataset
dvc remote list
gcloud alpha storage ls gs://backend-datastore
gcloud alpha storage cp gs://backend-datastore/* data
dvc add -R data/
```

```sh
kubectl create namespace bucket-namespace
kubectl create serviceaccount --namespace bucket-namespace bucket-service-account
gcloud iam service-accounts create google-bucket-service-account
gcloud iam service-accounts add-iam-policy-binding --role roles/iam.workloadIdentityUser --member "serviceAccount:awesome-project.svc.id.goog[bucket-namespace/bucket-service-account]" google-bucket-service-account@awesome-project.iam.gserviceaccount.com
kubectl annotate serviceaccount --namespace bucket-namespace bucket-service-account iam.gke.io/gcp-service-account=google-bucket-service-account@awesome-project-ID.iam.gserviceaccount.com
```
