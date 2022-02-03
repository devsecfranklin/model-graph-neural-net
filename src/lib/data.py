"""Deep Learning GNN testing."""
import fnmatch
import json
import os
import pathlib
import sys
import uuid
from pathlib import Path

import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from google.cloud import storage


class DataHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    my_uuid = ""  # set a unique filename
    repo_name = "example"  # repo name can help with de-duplication

    json_filename = ".metadata.json"
    dot_filename = ""  # set a unique dot filename
    png_filename = ""  # set a unique dot filename
    plt_filename = ""  # redraw graph with matplotlib
    tf_out_file = "tfout.txt"

    dot_files = []
    data_file_list = []

    def generate_uuid(self):
        """Generate a UUID for the graph a name.

        check_uuid : str
        version : {1, 2, 3, 4}
        """

        my_uuid = str(uuid.uuid4())  # set a unique filename
        # logger.debug("Generated a new UUID: ", my_uuid)
        self.my_uuid = my_uuid

        return my_uuid

    def update_repo_name(self, workdir, description_file):
        """Check .git/description to see if there is a name there, otherwise try to update it."""
        json_file = workdir + ".metadata.json"
        description_file = "../.git/description"

        path = Path(json_file)

    def update_metadata(self, workdir):
        """Update the JSON file with metadata/labels

        Args:
             workdir ([type]): [description]
        """
        data = {}  # hold the JSON values

        json_file = workdir + ".metadata.json"
        path = Path(json_file)

        if path.is_file():
            #    #logger.info("Update existing JSON")
            try:
                with open(json_file) as json_file:  # read in existing first
                    data = json.load(json_file)
                    # logger.debug('Existing JSON: ' + data['uuid']) # update the key value pairs
                    self.my_uuid = data["uuid"]
                    self.repo_name = data["repo_name"]
                json_file.close()
            except json.decoder.JSONDecodeError as e:
                print("JSON file is corrupted: ", e)
                sys.exit(1)
        else:
            try:
                self.generate_uuid()
                data["uuid"] = self.my_uuid
                data["repo_name"] = self.repo_name
                with open(
                    str(json_file), "w", encoding="utf-8"
                ) as f:  # write to the JSON file
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except TypeError as e:
                print("Caught a TypeError, ", e)

        self.json_filename = self.my_uuid + ".metadata.json"
        self.dot_filename = self.my_uuid + ".dot"
        self.png_filename = self.my_uuid + ".png"
        self.plt_filename = self.my_uuid + "-plt.png"
        self.tf_out_file = self.my_uuid + ".tfout.txt"
        self.data_file_list = [
            self.dot_filename,
            self.png_filename,
            self.plt_filename,
            self.tf_out_file,
        ]

        return self.data_file_list  # for consumption by common lib

    def graph_generate(self, my_dir):
        """Give the graph a name. Reuse the exisiting name if possible.

        check_uuid : str
        version : {1, 2, 3, 4}
        """
        dot_files = []

        for file in os.listdir(my_dir):
            if fnmatch.fnmatch(file, "*.dot"):
                dot_files.append(file)

        # for item in dot_files: # check for a dot and png file in workdir

        # if they exist, write to self.my_filename
        pass

    def generate_dot(self, workdir, tf_output):
        """Write the dot file to local filesystem.
        Return a pygraphviz object
        """
        try:
            # could name file based on tf
            text_file = open(workdir + self.dot_filename, "w")
            text_file.write(tf_output)
            text_file.close()
        except Exception as e:
            print("There was some error writing the graph dot file", e)

        gv = pgv.AGraph(
            workdir + self.dot_filename, strict=False, directed=True
        )  # convert dot file to pygraphviz format

        return gv

    def gather_dotfiles(self, workdir):
        """ """
        for f in os.listdir(workdir):
            # logger.debug("Found file: %s%s", self.input_path, f)
            if f.endswith(".dot"):
                # logger.info("Found dotfile {}'.format(f))
                self.dot_files.append(f)  # looks like O(n)

    def create_graph(self, workdir, dot):
        gv = pgv.AGraph(
            workdir + dot, strict=False, directed=True
        )  # convert dot file to pygraphviz format

        return gv

    def detect_isometry(self):
        """If two graphs (dot files) are isometric, delete one from dataset."""
        pass


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
