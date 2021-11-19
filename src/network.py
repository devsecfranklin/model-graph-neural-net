"""Deep Learning GNN testing."""
import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from python_terraform import Terraform


def collect_digraph_from_terraform():
    """Terraform can output a directed graph.

    Command line examples for png and svg format
    # terraform graph | dot -Tpng > graph.png
    # terraform graph | dot -Tsvg -o graph.svg
    """
    t = Terraform()
    return_code,  stdout, stderr = t.graph(capture_output=True)  # returns str

    return stdout


def write_dot_file(tf_output):
    """Write the dot file to local filesystem."""
    text_file = open("graph.dot", "w")  # could name file based on tf
    text_file.write(tf_output)
    text_file.close()


def main():
    """Testing Deep Learning with Graph Neural Networks."""
    tf_output = collect_digraph_from_terraform()  # get digraph from tf plan
    write_dot_file(tf_output)  # write the terraform digraph to a dot file
    gv = pgv.AGraph(
        "graph.dot", strict=False, directed=True
    )  # convert dot file to pygraphviz format
    G = nx.DiGraph(gv)  # Networkx can accept the pygraphviz dot formay
    nx.list(G.nodes(data=True))

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png")


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin D.'
__version__    = '0.1'
__email__      = 'frank378@gmail.com'
"""
