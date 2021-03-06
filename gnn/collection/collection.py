"""Gather data from Terraform files."""
import os

from gnn.lib.common import CommonHelpers
from gnn.lib.data import DataHelpers, DataObject
from gnn.lib.terraform import TerraformHelpers


def main():

    common_helper = CommonHelpers()
    data_helper = DataHelpers()
    data_object = DataObject()
    tf_helper = TerraformHelpers()

    workdir = os.getcwd() + "/.model/"

    common_helper.print_logo()  # make a nice logo on the console

    common_helper.print_output("Checking Terraform readiness...")
    tf_helper.check_init()

    common_helper.print_output("Checking for model directory...")
    created = common_helper.make_directory(
        workdir
    )  # create the working directory if needed
    if created:
        # we know we need to create a new json file
        common_helper.print_output("Creating model directory.")
        data_helper.generate_uuid()  # the value is saved to a var in helper class

    common_helper.print_output("Create/update metadata...")
    data_object = data_helper.update_metadata(workdir, data_object)  # pass working dir
    data_file_list = [
        data_object.dot_filename,
        data_object.png_filename,
        data_object.plt_filename,
        data_object.tf_out_file,
    ]

    common_helper.print_output("Collecting digraph...")
    tf_output = tf_helper.collect_digraph_from_terraform()  # get digraph from tf plan

    """Capture and write the response for Terraform. 
     
    Using for troubleshooting but we could read the respone and react appropriately, 
    (do a 'terraform init' for example)
    """
    common_helper.print_output("Write the response from Terraform to model dir.")
    file1 = open(workdir + data_object.tf_out_file, "w")
    file1.write(tf_output)
    file1.close()

    common_helper.print_output("Write the digraph to a dot file...")
    gv = data_helper.generate_dot(
        workdir, tf_output, data_object.dot_filename
    )  # write the terraform digraph to a dot file
    common_helper.print_output("Generating PNG file...")
    gv.draw(
        workdir + data_object.my_uuid + ".png", format="png", prog="dot"
    )  # make a nice picture in PNG format

    """Write data to GCP storage bucket. 
    We can disable local writes soon, and (continuous) cleaning/training can happen from bucket.
    """
    bucket_name = "backend-datastore"
    folder_name = "test1/"  # testing with a top level folder in storage bucket

    try:
        # print ('source file {}'.format(source_file_name))
        common_helper.print_output("Uploading JSON Metadata")
        common_helper.upload_blob(
            bucket_name,
            workdir + ".metadata.json",
            folder_name + data_object.json_filename,
        )
        common_helper.print_output("Uploading dot file.")
        common_helper.upload_blob(
            bucket_name,
            workdir + data_object.dot_filename,
            folder_name + data_object.dot_filename,
        )
        common_helper.print_output("Uploading PNG.")
        common_helper.upload_blob(
            bucket_name,
            workdir + data_object.png_filename,
            folder_name + data_object.png_filename,
        )
        common_helper.print_output("Uploading Lock.")
        common_helper.upload_blob(
            bucket_name,
            tf_helper.lock_file,
            folder_name + data_object.my_uuid + tf_helper.lock_file,
        )  # get TF lock file
        common_helper.print_output("Uploading State.")
        common_helper.upload_blob(
            bucket_name,
            tf_helper.state_file,
            folder_name + data_object.my_uuid + ".terraform.tfstate",
        )  # get TF state file
    except Exception as e:
        print("Problem uploading data: {}", e)

    common_helper.print_output("Cleaning up session.")
    common_helper.remove_workdir_files(
        workdir, data_file_list
    )  # erase the files after upload, except the .metadata.json

    common_helper.print_output("Success!")


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = 'Franklin <2730246+devsecfranklin@users.noreply.github.com>'
"""
