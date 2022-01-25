"""Deep Learning GNN testing."""
import uuid
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from python_terraform import Terraform
import pathlib

import fnmatch
import os
import sys
import time

class CollectionHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    current_dir = str(pathlib.Path(__file__).parents[1])
    workdir = current_dir + '/model'
    my_filename = str(uuid.uuid4())  # set a unique filename
    dot_filename = my_filename + ".dot"  # set a unique dot filename
    png_filename = my_filename + ".png"  # set a unique dot filename
    plt_filename = my_filename + "-plt.png" # redraw graph with matplotlib

    def configure_graph_name(self):
        """Give the graph a name. Reuse the exisiting name if possible.

        check_uuid : str
        version : {1, 2, 3, 4}
        """
        dot_files = []

        for file in os.listdir(self.workdir):
            if fnmatch.fnmatch(file, '*.dot'):
                dot_files.append(file)
        
        #for item in dot_files: # check for a dot and png file in workdir   

        try:
            uuid.UUID(check_uuid, version='4')
        except ValueError as e:
            print("Generating a new UUID: ", e)

        # if they exist, write to self.my_filename
        pass

    def collect_digraph_from_terraform(self):
        """Terraform can output a directed graph.

        Command line examples for png and svg format
        # terraform graph | dot -Tpng > graph.png
        # terraform graph | dot -Tsvg -o graph.svg
        """
        t = Terraform(terraform_bin_path='/usr/local/bin/terraform')
        return_code, stdout, stderr = t.graph(capture_output=True)  # returns str

        if stderr:
            #print(stderr)  # we could automatically run the init at this point?
            return stderr

        return stdout

    def process_output(self, file_path):
        """
        """
        pass

    def generate_dot(self, tf_output):
        """Write the dot file to local filesystem.
        Return a pygraphviz object
        """
        try:
            text_file = open(self.current_dir + '/' + self.workdir + '/' + self.dot_filename, "w")  # could name file based on tf
            text_file.write(tf_output)
            text_file.close()
        except Exception as e:
            print("There was some error writing the graph dot file", e)

        gv = pgv.AGraph(
            self.current_dir + '/' + self.workdir + '/' + self.dot_filename, strict=False, directed=True
        )  # convert dot file to pygraphviz format

        return gv

    def make_directory(self, my_dir):
        """Make a directory if it does not already exist."""
        try:
            os.mkdir(my_dir)
            #logger.debug("Created directory: %s", my_dir)
            print ("Created directory: " + my_dir)
        except FileNotFoundError as e:
            #logger.error("Unable to create directory %s because: %s", my_dir, e)
            print("Unable to create directory %s because: %s", my_dir, e)
        except FileExistsError as fe:
            #logger.error("Unable to create directory %s because it already exists.", my_dir)
            print("Unable to create directory " + my_dir + " because it already exists.")


    def print_output(self, message):
        """Print a message to the console."""
        sys.stdout.write("\033[K")
        message = "\033[5;36;40m" + message + "\033[0;0m"
        print(message, end="\r", flush=True)
        time.sleep(1)

"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
