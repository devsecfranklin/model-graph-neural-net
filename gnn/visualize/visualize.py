"""Testing Deep Learning with Graph Neural Networks."""
import os

import matplotlib.pyplot as plt  # this is for making the graph
import networkx as nx
import numpy as np
import pandas as pd
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from networkx.drawing.nx_agraph import graphviz_layout, write_dot

from lib.common import CommonHelpers
from lib.data import DataHelpers, DataObject


def main():
    """Testing Deep Learning with Graph Neural Networks."""
    data_helper = DataHelpers()
    data_object = DataObject()
    common_helper = CommonHelpers()

    # load the data files in from datastore
    workdir = os.getcwd() + "/dataset/"
    # logger.debug
    print("Using workdir: {}".format(workdir))
    created = common_helper.make_directory(
        workdir
    )  # create the working directory if needed

    data_helper.gather_dotfiles(workdir)

    for dot in data_helper.dot_files:
        print("Processing dot file: {}".format(dot))
        this_uuid = dot.split(".")
        data_obj = DataObject()
        data_obj.my_uuid = this_uuid[0]

        gv = data_helper.create_graph(
            workdir, dot
        )  # write the terraform digraph to a dot file

        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
        G = nx.DiGraph(
            gv, name=data_obj.my_uuid, node_color="tab:red", **options
        )  # Networkx can accept the pygraphviz dot format

        pos = nx.get_node_attributes(G, "pos")
        print(str(pos))
        if not pos:
            pos = graphviz_layout(G, prog="dot")

        edge_labels = nx.get_edge_attributes(G, "label")

        nx.draw(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
        nx.draw_networkx_labels(G, pos, font_size=10)
        G = nx.convert_node_labels_to_integers(
            G, first_label=0, ordering="default", label_attribute="orig_label"
        )

        nx.drawing.nx_pydot.write_dot(G, workdir + data_obj.my_uuid + ".test.dot")

        #########
        # Nodes #
        #########
        nodelist = list(G.nodes(data=True))
        # print(nodelist)
        print(
            "+++++ Sorted nodelist +++++\n", sorted(d for n, d in G.degree())
        )  # sorted list
        # print(nx.clustering(DG))  # cluster list
        # print("Number of nodes: ", DG.number_of_nodes()) # write this into metadata file?
        # print("Number of edges: ", DG.number_of_edges())
        data_obj.density = G.number_of_edges() / (
            G.number_of_nodes() * (G.number_of_nodes() - 1)
        )
        print(
            "Graph density: ", data_obj.density
        )  # d (0 ≤ d ≤ 1 ) tells how close a graph is to being "complete"

        # diameter D is the largest distance between any two nodes in the graph

        ##########################################
        # convert nx digraph to pandas dataframe #
        ##########################################
        # df = nx.to_pandas_dataframe(DG)
        df = pd.DataFrame.from_dict(dict(G.nodes(data=True)), orient="index")
        print("+++++ Pandas Dataframe Values +++++\n", df.values)

        plt.savefig(workdir + data_obj.my_uuid + ".plt.png")
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
__email__      = ''
"""
