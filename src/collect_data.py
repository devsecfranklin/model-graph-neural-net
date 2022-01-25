"""Gather data from Terraform files."""
from lib.collection_helpers import CollectionHelpers
import os


def main():
    my_helper = CollectionHelpers()

    my_helper.make_directory(os.getcwd() + '/model') # create the working directory if needed
    my_helper.configure_graph_name # find existing data in working dir, if any
    tf_output = my_helper.collect_digraph_from_terraform()  # get digraph from tf plan

    file1 = open(os.getcwd() + "model/tfout.txt", "w")
    file1.write(tf_output)
    file1.close()

    gv = my_helper.generate_dot(tf_output)  # write the terraform digraph to a dot file
    gv.draw(my_helper.png_filename, format="png", prog="dot")  # make a nice picture in PNG format


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
