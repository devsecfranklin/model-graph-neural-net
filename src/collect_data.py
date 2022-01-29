"""Gather data from Terraform files."""
import os

from lib.collection_helpers import CollectionHelpers
from lib.terraform_helpers import TerraformHelpers


def main():
    my_helper = CollectionHelpers()
    tf_helper = TerraformHelpers()
    workdir = os.getcwd() + "/.model/"

    my_helper.print_logo()

    my_helper.print_output("Checking Terraform readiness...")
    tf_helper.check_init()

    my_helper.print_output("Checking for model directory...")
    created = my_helper.make_directory(
        workdir
    )  # create the working directory if needed
    if created:
        # we know we need to create a new json file
        my_helper.print_output("Creating model directory.")
        my_helper.generate_uuid()  # the value is saved to a var in helper class

    my_helper.print_output("Create/update metadata...")
    my_helper.update_metadata(workdir)  # pass working dir

    my_helper.print_output("Collecting digraph...")
    tf_output = tf_helper.collect_digraph_from_terraform()  # get digraph from tf plan

    """Capture and write the response for Terraform. 
     
    Using for troubleshooting but we could read the respone and react appropriately, 
    (do a 'terraform init' for example)
    """
    my_helper.print_output("Write the response from Terraform to model dir.")
    file1 = open(workdir + my_helper.tf_out_file, "w")
    file1.write(tf_output)
    file1.close()

    my_helper.print_output("Write the digraph to a dot file...")
    gv = my_helper.generate_dot(
        workdir, tf_output
    )  # write the terraform digraph to a dot file
    my_helper.print_output("Generating PNG file...")
    gv.draw(
        workdir + my_helper.my_uuid + ".png", format="png", prog="dot"
    )  # make a nice picture in PNG format

    """Write data to GCP storage bucket. 
    We can disable local writes soon, and (continuous) cleaning/training can happen from bucket.
    """
    bucket_name = "backend-datastore"

    try:
        # print ('source file {}'.format(source_file_name))
        my_helper.print_output("Uploading JSON Metadata")
        my_helper.upload_blob(
            bucket_name, workdir + ".metadata.json", my_helper.json_filename
        )
        my_helper.print_output("Uploading dot file.")
        my_helper.upload_blob(
            bucket_name, workdir + my_helper.dot_filename, my_helper.dot_filename
        )
        my_helper.print_output("Uploading PNG.")
        my_helper.upload_blob(
            bucket_name, workdir + my_helper.png_filename, my_helper.png_filename
        )
        my_helper.print_output("Uploading Lock.")
        my_helper.upload_blob(
            bucket_name, tf_helper.lock_file, my_helper.my_uuid + tf_helper.lock_file
        )  # get TF lock file
        my_helper.print_output("Uploading State.")
        my_helper.upload_blob(
            bucket_name, tf_helper.state_file, my_helper.my_uuid + ".terraform.tfstate"
        )  # get TF state file
    except Exception as e:
        print("Problem uploading data: {}", e)

    my_helper.print_output("Cleaning up session.")
    my_helper.remove_workdir_files(
        workdir
    )  # erase the files after upload, except the .metadata.json

    my_helper.print_output("Success!")


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
