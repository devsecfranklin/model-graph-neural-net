"""Deep Learning GNN testing."""

import os
import pathlib
import sys
import time
from pathlib import Path

import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from google.cloud import storage
from python_terraform import Terraform

"""
import logging
import logging.config
logging.config.fileConfig(
    "logging.conf",
    defaults={"logfilename": "training.log"},
    disable_existing_loggers=True, # this will prevent modules from writing to our logger
)
logger = logging.getLogger("train")
"""


class CommonHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    current_dir = str(pathlib.Path(__file__).parents[1])

    def print_logo(self):
        """Display logo."""
        # logger.debug("Starting print_help().")
        my_file = open(self.current_dir + "/logo.txt")

        print(" ")
        print("-" * 80)
        for line in my_file:
            print(line.rstrip())
        print("-" * 80 + "\n\n")

    def print_output(self, message):
        """Print a message to the console."""
        sys.stdout.write("\033[K")
        message = "\033[5;36;40m" + message + "\033[0;0m"
        print(message, end="\r", flush=True)
        time.sleep(1)

    def pull_data_from_bucket(self):
        """
        gsutil -m cp -r gs://backend-datastore/* .
        """
        print("")

    def make_directory(self, my_dir):
        """Make a directory if it does not already exist.

        return a boolean if created
        """
        created = False

        try:
            os.mkdir(my_dir)
            # logger.debug("Created directory: %s", my_dir)
            print("Created directory: " + my_dir)
            created = True
        except FileNotFoundError as e:
            # logger.error("Unable to create directory %s because: %s", my_dir, e)
            print("Unable to create directory %s because: %s", my_dir, e)
        except FileExistsError as fe:
            # logger.error("Unable to create directory %s because it already exists.", my_dir)
            # print("Unable to create directory " + my_dir + " because it already exists.")
            pass  # this is OK
        return created

    def upload_blob(self, bucket_name, source_file_name, destination_blob_name):
        """Upload files to data store.

        The encryption_key should be a str or bytes with a length of at least 32.
        """
        encryption_key = "c7f32af42e45e85b9848a6a14dd2a8f6"  #
        storage_client = storage.Client.from_service_account_json(
            "/home/franklin/.config/gcloud/franklin-storage-key.json"
        )
        bucket = storage_client.get_bucket(bucket_name)
        # blob = Blob("secure-data", bucket, encryption_key=encryption_key)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))

    def download_to_local(self, workdir, bucket_name, prefix):
        """[summary]

        Args:
            workdir ([type]): [description]
            bucket_name ([type]): [description]
            remote_folder ([type]): [description]
        """
        print("Call to download_to_local() with {}".format(workdir))

        storage_client = storage.Client.from_service_account_json(
            "/home/franklin/.config/gcloud/franklin-storage-key.json"
        )
        bucket = storage_client.get_bucket(bucket_name)

        delimiter = "/"

        for blob in bucket.list_blobs(max_results=10, prefix=prefix):
            if not blob.name.endswith(delimiter):
                name = blob.name.split(delimiter)
                print("Download {}".format(workdir + name[-1]))
                try:
                    blob.download_to_filename(workdir + name[-1])
                except Exception as e:
                    print(e)

    def remove_workdir_files(self, workdir, data_file_list):
        """erase the files after upload, except the .json.metadata"""
        try:
            for data_file in data_file_list:
                # logger.info('Attempt to remove data_file: {} '.format(data_file))
                path = Path(workdir + data_file)
                if path.is_file():
                    os.remove(path)
        except Exception as e:
            print("Unable to remove data_file: {} ".format(e))


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
