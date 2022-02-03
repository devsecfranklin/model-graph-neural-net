FROM gcr.io/deeplearning-platform-release/tf-gpu.2-7
COPY . /train

RUN python -m pip install -r /train/src/requirements.txt

# pull in data from gs://backend-dataset

CMD ["python", "/train/src/train.py"]
