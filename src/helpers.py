"""Deep Learning GNN testing."""
import pygraphviz as pgv  # sudo apt install libgraphviz-dev
from python_terraform import Terraform


class FranklinHelpers:
    """

    # https://github.com/pyjanitor-devs/pyjanitor
    # import janitor  # upon import, functions are registered as part of pandas.
    """

    def collect_digraph_from_terraform(self):
        """Terraform can output a directed graph.

        Command line examples for png and svg format
        # terraform graph | dot -Tpng > graph.png
        # terraform graph | dot -Tsvg -o graph.svg
        """
        t = Terraform(terraform_bin_path='/usr/bin/terraform')
        return_code, stdout, stderr = t.graph(capture_output=True)  # returns str

        if stderr:
            print(stderr)  # we could automatically run the init at this point?
            exit(1)

        return stdout

    def generate_dot(self, tf_output):
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
