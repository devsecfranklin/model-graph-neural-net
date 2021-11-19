"""Deep Learning GNN testing."""
import matplotlib.pyplot as plt  # this is for making the graph
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
    return_code, stdout, stderr = t.graph(capture_output=True)  # returns str

    if stderr:
        print(stderr)  # we could automatically run the init at this point?
        exit(1)

    return stdout


def generate_dot(tf_output):
    """Write the dot file to local filesystem.
    Return a pygraphviz object
    """
    try:
        text_file = open("graph.dot", "w")  # could name file based on tf
        text_file.write(tf_output)
        text_file.close()
    except Exception as e:
        print("There was some error writing the graph dot file", e)

    gv = pgv.AGraph(
        "graph.dot", strict=False, directed=True
    )  # convert dot file to pygraphviz format

    return gv


def main():
    """Testing Deep Learning with Graph Neural Networks."""
    tf_output = collect_digraph_from_terraform()  # get digraph from tf plan

    gv = generate_dot(tf_output)  # write the terraform digraph to a dot file
    gv.draw("graph.png", format="png", prog="dot")  # optional PNG output

    DG = nx.DiGraph(
        gv, name="Franklin"
    )  # Networkx can accept the pygraphviz dot format

    nodelist = list(DG.nodes(data=True))

    # print(nodelist)
    print(sorted(d for n, d in DG.degree()))  # sorted list
    print(nx.clustering(DG))  # cluster list

    # Adjacency Matrix
    numpy_recarray = nx.to_numpy_matrix(DG)  # graph adjacency matrix as a NumPy matrix.
    am = nx.adjacency_matrix(DG)  # requires scipy module
    # print(am)
    print(am.todense())
    am.setdiag(am.diagonal() * 2)
    print(am.todense())

    # Incidence Matrix
    im = nx.incidence_matrix(DG)
    print(im.todense())

    # Laplacian Matrix
    # lm = nx.laplacian_matrix(DG)


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin D.'
__version__    = '0.1'
__email__      = 'frank378@gmail.com'
"""
