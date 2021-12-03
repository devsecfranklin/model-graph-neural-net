"""Deep Learning GNN testing."""
import uuid
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from python_terraform import Terraform

import fnmatch
import os

class FranklinHelpers:
    """

    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

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
        for file in os.listdir('.'):
            if fnmatch.fnmatch(file, '*.dot'):
                dot_files.append(file)
        for dot in dot_files:
            
        
        # check for a dot and png file in current directory.
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
        t = Terraform(terraform_bin_path="/usr/local/bin/terraform")
        return_code, stdout, stderr = t.graph(capture_output=True)  # returns str

        if stderr:
            print(stderr)  # we could automatically run the init at this point?
            exit(1)

        return stdout

    def generate_dot(self, tf_output):
        """Write the dot file to local filesystem.
        Return a pygraphviz object
        """
        try:
            text_file = open(self.dot_filename, "w")  # could name file based on tf
            text_file.write(tf_output)
            text_file.close()
        except Exception as e:
            print("There was some error writing the graph dot file", e)

        gv = pgv.AGraph(
            self.dot_filename, strict=False, directed=True
        )  # convert dot file to pygraphviz format

        return gv

    def detect_isometry(self):
        """If two graphs (dot files) are isometric, delete one from dataset."""
        pass


"""
__author__     = 'Franklin Diaz'
__version__    = '0.1'
__email__      = 'fdiaz@paloaltonetworks.com'
"""
