"""Testing Deep Learning with Graph Neural Networks."""
import logging
import logging.config
import os

import matplotlib.pyplot as plt  # this is for making the graph
import networkx as nx
import numpy as np
import pandas as pd
import pygraphviz as pgv  # sudo apt install libgraphviz-dev

from lib.common import CommonHelpers
from lib.data import DataHelpers
from lib.terraform import TerraformHelpers

logging.config.fileConfig(
    "logging.conf",
    defaults={"logfilename": "project.log"},
    disable_existing_loggers=False,
)
logger = logging.getLogger("__name__")


def main():
    """Testing Deep Learning with Graph Neural Networks."""
    data_helper = DataHelpers()
    common_helper = CommonHelpers()

    # load the data files in from datastore
    workdir = os.getcwd() + "/dataset/"
    logger.debug('Using workdir: {}'.format(workdir))
    created = common_helper.make_directory(
        workdir
    )  # create the working directory if needed

    data_helper.gather_dotfiles(workdir)

    for dot in data_helper.dot_files:
        logger.debug('Processing dot file: {}'.format(dot))
        this_uuid = dot.split('.')
        gv = data_helper.create_graph(
            workdir, dot
        )  # write the terraform digraph to a dot file

        DG = nx.DiGraph(
            gv, name=this_uuid[0]
        )  # Networkx can accept the pygraphviz dot format

        #########
        # Nodes #
        #########
        nodelist = list(DG.nodes(data=True))
        # print(nodelist)
        print(
            "+++++ Sorted nodelist +++++\n", sorted(d for n, d in DG.degree())
        )  # sorted list
        # print(nx.clustering(DG))  # cluster list
        print("Number of nodes: ", DG.number_of_nodes())
        print("Number of edges: ", DG.number_of_edges())
        density = DG.number_of_edges() / (DG.number_of_nodes() * (DG.number_of_nodes( ) - 1 ) ) 
        print('Graph density: ', density) # d (0 ≤ d ≤ 1 ) tells how close a graph is to being "complete"

        # diameter D is the largest distance between any two nodes in the graph
    
        ##########################################
        # convert nx digraph to pandas dataframe #
        ##########################################
        # df = nx.to_pandas_dataframe(DG)
        df = pd.DataFrame.from_dict(dict(DG.nodes(data=True)), orient="index")
        print("+++++ Pandas Dataframe Values +++++\n", df.values)

        #################
        # Relabel Graph #
        #################
        DG = nx.convert_node_labels_to_integers(
            DG, first_label=0, ordering="default", label_attribute="orig_label"
        )
        nx.draw(DG, with_labels=True, node_color="#4bbefd")
        plt.savefig(workdir + this_uuid[0] + '.plt.png')
        # plt.show() # use this in Jupyter

        ####################
        # Adjacency Matrix #
        ####################
        A = nx.adjacency_matrix(DG)  # requires scipy module
        # print(am)
        # print(A.todense())
        # A.setdiag(A.diagonal() * 2)
        print("+++++ Adjacency Matrix ++++\n", A)
        print("+++++ Dense Adj Matrix +++++\n", A.todense())

        ####################
        # Incidence Matrix #
        ####################
        I = nx.incidence_matrix(DG)
        print("+++++ Incidence Matrix +++++\n", I)
        print("+++++ Dense Incidence Matrix +++++\n", I.todense())

        """ Degree Matrix 
    
	    Adding the inverse of the degree matrix ensures inclusion of root node.
        """

        # Laplacian Matrix (L = D - A)
        # L = nx.laplacian_matrix(DG)

        numpy_recarray = nx.to_numpy_matrix(
            DG
        )  # graph adjacency matrix as a NumPy matrix.
        AA = np.matrix(numpy_recarray)
        X = np.matrix([[i, -i] for i in range(AA.shape[0])], dtype=float)
        print(A * X)  # apply propagation rule


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
