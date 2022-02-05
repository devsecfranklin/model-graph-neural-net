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


class DataObject:
    """A single graph from our data set."""

    def __init__(
        self,
        my_uuid=None,
        repo_name=None,
        json_filename=None,
        dot_filename=None,
        png_filename=None,
        plt_filename=None,
        tf_out_file=None,
        node_count=None,
        edge_count=None,
        density=None,
        completeness_score=None,
    ):
        self.my_uuid = my_uuid  # set a unique filename
        self.repo_name = repo_name  # repo name can help with de-duplication
        self.json_filename = json_filename  # ".metadata.json"
        self.dot_filename = dot_filename  # set a unique dot filename
        self.png_filename = png_filename  # set a unique dot filename
        self.plt_filename = plt_filename  # redraw graph with matplotlib
        self.tf_out_file = tf_out_file  # "tfout.txt"
        self.node_count = node_count
        self.edge_count = edge_count
        self.density = density
        self.completeness_score = completeness_score


class DataHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    def __init__(self):
        self.data_object = None

    my_uuid = ""  # set a unique filename
    repo_name = "example"  # repo name can help with de-duplication

    dot_files = []

    def data_obj_update(self, workdir, data_object):
        data = {}  # hold the JSON values

        data_object.json_file = workdir + ".metadata.json"

        path = Path(self.json_file)
        if path.is_file():
            #    #logger.info("Update existing JSON")
            try:

                data["node_count"] = data_object.node_count
                data["edge_count"] = data_object.edge_count
                data["density"] = data_object.density
                data["completeness_score"] = data_object.completeness_score
                with open(
                    str(self.json_file), "w", encoding="utf-8"
                ) as f:  # write to the JSON file
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except json.decoder.JSONDecodeError as e:
                print("JSON file is corrupted: ", e)
                sys.exit(1)

    def generate_uuid(self):
        """Generate a UUID for the graph a name.

        check_uuid : str
        version : {1, 2, 3, 4}
        """

        my_uuid = str(uuid.uuid4())  # set a unique filename
        # logger.debug("Generated a new UUID: ", my_uuid)

        return my_uuid

    def update_repo_name(self, workdir, description_file):
        """Check .git/description to see if there is a name there, otherwise try to update it."""
        json_file = workdir + ".metadata.json"
        description_file = "../.git/description"

        path = Path(json_file)

    def update_metadata(self, workdir, data_object):
        """Update the JSON file with metadata/labels

        Args:
             workdir ([type]): [description]
        """
        data = {}  # hold the JSON values

        json_file = workdir + ".metadata.json"
        path = Path(json_file)

        my_uuid = self.generate_uuid()  # pre-load a new UUID but we may not need it

        if path.is_file():
            #    #logger.info("Update existing JSON")
            try:
                with open(json_file) as json_file:  # read in existing first
                    data = json.load(json_file)
                    # logger.debug('Existing JSON: ' + data['uuid']) # update the key value pairs
                    my_uuid = data["uuid"]
                    data_object.my_uuid = data["uuid"]
                    data_object.repo_name = data["repo_name"]
                json_file.close()
            except json.decoder.JSONDecodeError as e:
                print("JSON file is corrupted: ", e)
                sys.exit(1)
        else:
            try:
                data["uuid"] = my_uuid
                data["repo_name"] = "repo_name"  # call update_repo_name instead
                with open(
                    str(json_file), "w", encoding="utf-8"
                ) as f:  # write to the JSON file
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except TypeError as e:
                print("Caught a TypeError, ", e)

        data_object.my_uuid = my_uuid
        data_object.json_filename = my_uuid + ".metadata.json"
        data_object.dot_filename = my_uuid + ".dot"
        data_object.png_filename = my_uuid + ".png"
        data_object.plt_filename = my_uuid + "-plt.png"
        data_object.tf_out_file = my_uuid + ".tfout.txt"

        return data_object

    def create_graph(self, workdir, dot):
        """Convert the initial Terraform DiGraph to graphviz format"""
        gv = pgv.AGraph(
            workdir + dot, strict=False, directed=True
        )  # convert dot file to pygraphviz format

        # http://www.graphviz.org/doc/info/attrs.html
        gv.graph_attr.update(
            landscape="true", ranksep="0.1"
        )  # Graphviz graph keyword parameters
        gv.node_attr.update(color="red")
        gv.edge_attr.update(len="2.0", color="blue")

        return gv

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

    def generate_dot(self, workdir, tf_output, dot_filename):
        """Write the dot file to local filesystem.
        Return a pygraphviz object
        """
        try:
            # could name file based on tf
            text_file = open(workdir + dot_filename, "w")
            text_file.write(tf_output)
            text_file.close()
        except Exception as e:
            print("There was some error writing the graph dot file", e)

        gv = pgv.AGraph(
            workdir + dot_filename, strict=False, directed=True
        )  # convert dot file to pygraphviz format
        # http://www.graphviz.org/doc/info/attrs.html
        gv.graph_attr.update(
            landscape="true", ranksep="0.1"
        )  # Graphviz graph keyword parameters
        gv.node_attr.update(color="red")
        gv.edge_attr.update(len="2.0", color="blue")
        return gv

    def gather_dotfiles(self, workdir):
        """ """
        for f in os.listdir(workdir):
            # logger.debug("Found file: %s%s", self.input_path, f)
            if f.endswith(".dot"):
                # logger.info("Found dotfile {}'.format(f))
                self.dot_files.append(f)  # looks like O(n)

    def detect_isometry(self):
        """If two graphs (dot files) are isometric, delete one from dataset."""
        pass


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
