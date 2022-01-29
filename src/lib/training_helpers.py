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
