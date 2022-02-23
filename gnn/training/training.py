"""Testing Deep Learning with Graph Neural Networks."""
import logging
import logging.config
import os
import sys

import matplotlib.pyplot as plt  # this is for making the graph
import networkx as nx
import numpy as np

# import pandas as pd
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from gnn.lib.common import CommonHelpers
from gnn.lib.data import DataHelpers, DataObject
from networkx.drawing.nx_agraph import graphviz_layout, write_dot

logging.config.fileConfig(
    "logging.conf",
    defaults={"logfilename": "training.log"},
    disable_existing_loggers=True,  # this will prevent modules from writing to our logger
)
logger = logging.getLogger("train")


def main():
    """Testing Deep Learning with Graph Neural Networks."""
    data_helper = DataHelpers()
    data_obj = DataObject()
    common_helper = CommonHelpers()

    # load the data files in from datastore
    workdir = os.getcwd() + "/dataset/"

    logger.info("Using workdir: {}".format(workdir))
    created = common_helper.make_directory(
        workdir
    )  # create the working directory if needed

    bucket_name = "backend-datastore"
    prefix = "test1/"  # testing with a top level folder in storage bucket
    # common_helper.download_to_local(workdir, bucket_name, prefix) # Make a flag for pulling remote data

    data_helper.gather_dotfiles(workdir)

    if data_helper.dot_files is None:
        logger.info("No data files found.")
        sys.exit(1)

    for dot in data_helper.dot_files:
        logger.info("Processing dot file: {}".format(dot))
        this_uuid = dot.split(".")
        data_obj = DataObject()
        data_obj.my_uuid = this_uuid[0]

        ##############
        # pygraphviz #
        ##############
        gv = data_helper.create_graph(
            workdir, dot
        )  # write the terraform digraph to a dot file

        ############
        # Networkx #
        ############
        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
        G = nx.DiGraph(
            gv, name=data_obj.my_uuid, node_color="tab:red", **options
        )  # Networkx can accept the pygraphviz dot format

        nodelist = list(G.nodes(data=True))
        # print(nodelist)
        print(
            "+++++ Sorted nodelist +++++\n", sorted(d for n, d in G.degree())
        )  # sorted list
        # logger.debug(nx.clustering(G))  # cluster list
        data_obj.node_count = G.number_of_nodes()
        logger.debug("Node count: {}".format(data_obj.node_count))
        data_obj.edge_count = G.number_of_edges()
        logger.debug("Edge count: {}".format(data_obj.edge_count))

        data_obj.density = G.number_of_edges() / (
            G.number_of_nodes() * (G.number_of_nodes() - 1)
        )
        logger.debug(
            "Graph density: {}".format(data_obj.density)
        )  # d (0 ≤ d ≤ 1 ) tells how close a graph is to being "complete"

        # diameter D is the largest distance between any two nodes in the graph

        data_helper.data_obj_update(
            workdir, data_obj
        )  # update the data file for this graph

        ##########################################
        # convert nx digraph to pandas dataframe #
        ##########################################
        # df = nx.to_pandas_dataframe(DG)
        # df = pd.DataFrame.from_dict(dict(G.nodes(data=True)), orient="index")
        # print("+++++ Pandas Dataframe Values +++++\n", df.values)

        # move this to the draw function
        # plt.savefig(workdir + data_obj.my_uuid + ".plt.png")
        # plt.show() # use this in Jupyter

        ####################
        # Adjacency Matrix #
        ####################
        A = nx.adjacency_matrix(G)  # requires scipy module
        # print(am)
        # print(A.todense())
        # A.setdiag(A.diagonal() * 2)
        print("+++++ Adjacency Matrix ++++\n", A)
        print("+++++ Dense Adj Matrix +++++\n", A.todense())

        ####################
        # Incidence Matrix #
        ####################
        I = nx.incidence_matrix(G)
        print("+++++ Incidence Matrix +++++\n", I)
        print("+++++ Dense Incidence Matrix +++++\n", I.todense())

        """ Degree Matrix 
    
	    Adding the inverse of the degree matrix ensures inclusion of root node.
        """

        # Laplacian Matrix (L = D - A)
        # L = nx.laplacian_matrix(DG)

        numpy_recarray = nx.to_numpy_matrix(
            G
        )  # graph adjacency matrix as a NumPy matrix.
        AA = np.matrix(numpy_recarray)
        X = np.matrix([[i, -i] for i in range(AA.shape[0])], dtype=float)
        print(A * X)  # apply propagation rule


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = 'Franklin <2730246+devsecfranklin@users.noreply.github.com>'
"""
