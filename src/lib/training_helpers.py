"""Deep Learning GNN testing."""
import uuid
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from python_terraform import Terraform
import pathlib

import fnmatch
import os
import sys
import time


class FranklinHelpers:
    """
    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """
 
    dot_files = []
    
    def pull_data_from_bucket(self):
    	"""
        gsutil -m cp -r gs://backend-datastore/* .
        """
        pass

    def gather_dotfiles(self, workdir):
        """
        """
        for f in os.listdir(workdir):
            # logger.debug("Found file: %s%s", self.input_path, f)
            if f.endswith(".dot"): 
                #logger.info("Found dotfile {}'.format(f))
                self.dot_files.append(f) # looks like O(n)

    def create_graph(self, workdir):
        gv = pgv.AGraph(
            workdir + self.dot_filename, strict=False, directed=True
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
