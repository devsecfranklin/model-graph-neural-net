import graphviz
from python_terraform import *

import networkx as nx
import matplotlib.pyplot as plt

import pygraphviz as pgv # sudo apt install libgraphviz-dev


# terraform graph | dot -Tpng > graph.png
# terraform graph | dot -Tsvg -o graph.svg
t = Terraform()
return_code, stdout, stderr = t.graph(capture_output=True) # this returns a string

text_file = open("graph.dot", "w")
n = text_file.write(stdout)
text_file.close()

gv = pgv.AGraph('graph.dot', strict=False, directed=True)
G = nx.DiGraph(gv)

nx.draw(G,with_labels=True)
plt.savefig("graph.png")
