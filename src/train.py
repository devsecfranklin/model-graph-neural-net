"""Testing Deep Learning with Graph Neural Networks."""
import logging
import logging.config
import os

import matplotlib.pyplot as plt  # this is for making the graph
import networkx as nx
import numpy as np
import pandas as pd
import pygraphviz as pgv  # sudo apt install libgraphviz-dev

from lib.training_helpers import FranklinHelpers
from lib.collection_helpers import CollectionHelpers

"""
logging.config.fileConfig(
    "logging.conf",
    defaults={"logfilename": "project.log"},
    disable_existing_loggers=False,
)
logger = logging.getLogger("__name__")
"""


def main():
    """Testing Deep Learning with Graph Neural Networks."""
    my_helper = FranklinHelpers()
    collection_helper = CollectionHelpers()

    # load the data files in from datastore
    workdir = os.getcwd() + "/data/"
    created = collection_helper.make_directory(
        workdir
    )  # create the working directory if needed

    # pull the data from datastore
    # gsutil -m cp -r gs://backend-datastore/* .
    my_helper.gather_dotfiles(workdir)

    for dot in my_helpers.dot_files:
        # Make the graph
        gv = my_helper.create_graph(workdir)  # write the terraform digraph to a dot file

        DG = nx.DiGraph(
            gv, name="Franklin"
        )  # Networkx can accept the pygraphviz dot format

        # Nodes
        nodelist = list(DG.nodes(data=True))
        # print(nodelist)
        print(
            "+++++ Sorted nodelist +++++\n", sorted(d for n, d in DG.degree())
        )  # sorted list
        # print(nx.clustering(DG))  # cluster list
        print("Number of nodes: ", DG.number_of_nodes())
        print("Number of edges: ", DG.number_of_edges())

    # convert nx digraph to pandas dataframe
    # df = nx.to_pandas_dataframe(DG)
    df = pd.DataFrame.from_dict(dict(DG.nodes(data=True)), orient="index")
    print("+++++ Pandas Dataframe Values +++++\n", df.values)

    # Relabel Graph
    DG = nx.convert_node_labels_to_integers(
        DG, first_label=0, ordering="default", label_attribute="orig_label"
    )
    nx.draw(DG, with_labels=True, node_color="#4bbefd")
    plt.savefig("graph3.png")  # if this is permanent, fix the filename
    # plt.show() # use this in Jupyter

    """Adjacency Matrix."""
    A = nx.adjacency_matrix(DG)  # requires scipy module
    # print(am)
    # print(A.todense())
    # A.setdiag(A.diagonal() * 2)
    print("+++++ Adjacency Matrix ++++\n", A)
    print("+++++ Dense Adj Matrix +++++\n", A.todense())

    # Incidence Matrix
    I = nx.incidence_matrix(DG)
    print("+++++ Incidence Matrix +++++\n", I)
    print("+++++ Dense Incidence Matrix +++++\n", I.todense())

    """ Degree Matrix 
    
	Adding the inverse of the degree matrix ensures inclusion of root node.
    """

    # Laplacian Matrix (L = D - A)
    # L = nx.laplacian_matrix(DG)

    numpy_recarray = nx.to_numpy_matrix(DG)  # graph adjacency matrix as a NumPy matrix.
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
