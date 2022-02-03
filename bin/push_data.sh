#!/bin/bash

#DATA_FILES=`gcloud alpha storage ls --recursive gs://backend-datastore/test1`

DATA_FILES=`ls dataset/`

for MY_FILE in ${DATA_FILES}
do
  gcloud alpha storage cp --recursive dataset/${MY_FILE} gs://backend-datastore/test1
done

# dvc add dataset/*.dvc
# git add dataset/*.dvc 