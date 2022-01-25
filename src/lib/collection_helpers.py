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

class CollectionHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    current_dir = str(pathlib.Path(__file__).parents[1]) # use this to save a copy of data to repo?
    workdir = './model'
    
    my_filename = str(uuid.uuid4())  # set a unique filename
    dot_filename = my_filename + ".dot"  # set a unique dot filename
    png_filename = my_filename + ".png"  # set a unique dot filename
    plt_filename = my_filename + "-plt.png" # redraw graph with matplotlib

    def generate_uuid(self):
        """Generate a UUID for the graph a name.

        check_uuid : str
        version : {1, 2, 3, 4}
        """
        print("Generating a new UUID", self.my_filename)

    def update_metadata(self, workdir):
        """Update the JSON file with metadata/labels

        Args:
             workdir ([type]): [description]
        """
        data = {} #hold the JSON values

        json_file = workdir + '/.json.metadata'
        path = Path(json_file)
        data['uuid'] = self.my_filename
        #json_data = json.dumps(data)

        #if path.is_file():
        #    print ("Update existing JSON")
        #    with open(json_file) as json_file: # read in existing first
        #        data = json.load(json_file)
        print('Existing JSON: ' + data['uuid']) # update the key value pairs

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def graph_generate(self, my_dir):
        """Give the graph a name. Reuse the exisiting name if possible.

        check_uuid : str
        version : {1, 2, 3, 4}
        """
        dot_files = []

        for file in os.listdir(my_dir):
            if fnmatch.fnmatch(file, '*.dot'):
                dot_files.append(file)
        
        #for item in dot_files: # check for a dot and png file in workdir   


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
        """Make a directory if it does not already exist.
        
        return a boolean if created
        """
        created = False

        try:
            os.mkdir(my_dir)
            #logger.debug("Created directory: %s", my_dir)
            print ("Created directory: " + my_dir)
            created = True
        except FileNotFoundError as e:
            #logger.error("Unable to create directory %s because: %s", my_dir, e)
            print("Unable to create directory %s because: %s", my_dir, e)
        except FileExistsError as fe:
            #logger.error("Unable to create directory %s because it already exists.", my_dir)
            print("Unable to create directory " + my_dir + " because it already exists.")
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

    def identify_provider(self):
        """Check to see which cloud provider this is.

        hashicorp/azurerm
        """
        pass

    def xmit_data():
        """Phone home with data/metadata.
        """
        pass

"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
