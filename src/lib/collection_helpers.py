"""Deep Learning GNN testing."""
import uuid
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from python_terraform import Terraform
import pathlib
from pathlib import Path
import json
import fnmatch
import os
import sys
import time
from google.cloud import storage


class CollectionHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    # use this to save a copy of data to repo?
    current_dir = str(pathlib.Path(__file__).parents[1])
    workdir = './model'

    my_uuid = ""  # set a unique filename
    json_filename = my_uuid + '.json.metadata'
    dot_filename = my_uuid + ".dot"  # set a unique dot filename
    png_filename = my_uuid + ".png"  # set a unique dot filename
    plt_filename = my_uuid + "-plt.png"  # redraw graph with matplotlib

    def generate_uuid(self):
        """Generate a UUID for the graph a name.

        check_uuid : str
        version : {1, 2, 3, 4}
        """

        my_uuid = str(uuid.uuid4())  # set a unique filename
        #logger.debug("Generated a new UUID: ", my_uuid)
        self.my_uuid = my_uuid

        return my_uuid

    def update_metadata(self, workdir):
        """Update the JSON file with metadata/labels

        Args:
             workdir ([type]): [description]
        """
        data = {}  # hold the JSON values

        json_file = workdir + '/.json.metadata'
        path = Path(json_file)

        if path.is_file():
            #    #logger.info("Update existing JSON")
            try:
                with open(json_file) as json_file:  # read in existing first
                    data = json.load(json_file)
                    # logger.debug('Existing JSON: ' + data['uuid']) # update the key value pairs

                    self.my_uuid = data['uuid']
                json_file.close()
            except json.decoder.JSONDecodeError as e:
                print("JSON file is corrupted: ", e)
                sys.exit(1)
        else:
            try:
                self.generate_uuid()
                data['uuid'] = self.my_uuid
                with open(str(json_file), 'w', encoding='utf-8') as f:  # write to the JSON file
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except TypeError as e:
                print("Caught a TypeError, ", e)

        self.json_filename = self.my_uuid

    def graph_generate(self, my_dir):
        """Give the graph a name. Reuse the exisiting name if possible.

        check_uuid : str
        version : {1, 2, 3, 4}
        """
        dot_files = []

        for file in os.listdir(my_dir):
            if fnmatch.fnmatch(file, '*.dot'):
                dot_files.append(file)

        # for item in dot_files: # check for a dot and png file in workdir

        # if they exist, write to self.my_filename
        pass

    def collect_digraph_from_terraform(self):
        """Terraform can output a directed graph.

        Command line examples for png and svg format
        # terraform graph | dot -Tpng > graph.png
        # terraform graph | dot -Tsvg -o graph.svg
        """
        t = Terraform(terraform_bin_path='/usr/local/bin/terraform')
        return_code, stdout, stderr = t.graph(
            capture_output=True)  # returns str

        if stderr:
            # print(stderr)  # we could automatically run the init at this point?
            return stderr

        return stdout

    def generate_dot(self, workdir, tf_output):
        """Write the dot file to local filesystem.
        Return a pygraphviz object
        """
        try:
            # could name file based on tf
            text_file = open(workdir + '/' + self.my_uuid + '.dot', "w")
            text_file.write(tf_output)
            text_file.close()
        except Exception as e:
            print("There was some error writing the graph dot file", e)

        gv = pgv.AGraph(
            workdir + '/' + self.my_uuid + '.dot', strict=False, directed=True
        )  # convert dot file to pygraphviz format

        return gv

    def make_directory(self, my_dir):
        """Make a directory if it does not already exist.

        return a boolean if created
        """
        created = False

        try:
            os.mkdir(my_dir)
            #logger.debug("Created directory: %s", my_dir)
            print("Created directory: " + my_dir)
            created = True
        except FileNotFoundError as e:
            #logger.error("Unable to create directory %s because: %s", my_dir, e)
            print("Unable to create directory %s because: %s", my_dir, e)
        except FileExistsError as fe:
            #logger.error("Unable to create directory %s because it already exists.", my_dir)
            #print("Unable to create directory " + my_dir + " because it already exists.")
            pass  # this is OK
        return created

    def print_logo(self):
        """Display logo."""
        #logger.debug("Starting print_help().")
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

    def upload_blob(self, bucket_name, source_file_name, destination_blob_name):
       
        #storage_client = storage.Client()
        storage_client = storage.Client.from_service_account_json('/home/franklin/.config/gcloud/franklin-storage-key.json')
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""

