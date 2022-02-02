#!/bin/bash

DATA_FILES=`gcloud alpha storage ls --recursive gs://backend-datastore/test1`

for MY_FILE in ${DATA_FILES}
do
  asdf=`echo $MY_FILE | cut -f2 -d'.' `
  if [ $asdf = "dot" ]; then
    newfile=`echo ${MY_FILE} | cut -f5 -d'/'`
    dvc get-url ${MY_FILE} dataset/${newfile}
  fi
done

# dvc add dataset/*.dvc
# git add dataset/*.dvc 
