"""Gather data from Terraform files."""
from lib.collection_helpers import CollectionHelpers
import os


def main():
    my_helper = CollectionHelpers()
    workdir = os.getcwd() + '/model'

    my_helper.print_logo()

    my_helper.print_output("Checking for model directory...")
    created = my_helper.make_directory(workdir) # create the working directory if needed
    if created:
        # we know we need to create a new json file
        my_helper.print_output("Creating model directory.")
        my_helper.generate_uuid() # the value is saved to a var in helper class

    my_helper.print_output("Create/update metadata...")
    my_helper.update_metadata(workdir) # pass working dir

    my_helper.print_output("Collecting digraph...")
    tf_output = my_helper.collect_digraph_from_terraform()  # get digraph from tf plan
    
    """Capture and write the response for Terraform. 
     
    Using for troubleshooting but we could read the respone and react appropriately, 
    (do a 'terraform init' for example)
    """
    my_helper.print_output("Write the response from Terraform to model dir.")
    file1 = open(workdir + "/tfout.txt", "w")
    file1.write(tf_output)
    file1.close()
    
    my_helper.print_output("Write the digraph to a dot file...")
    gv = my_helper.generate_dot(workdir, tf_output)  # write the terraform digraph to a dot file
    my_helper.print_output("Generating PNG file...")
    gv.draw(workdir + '/' + my_helper.my_uuid + '.png', format="png", prog="dot")  # make a nice picture in PNG format

    # Test bucket writes
    bucket_name = "backend-datastore"
    source_metadata = workdir + '/.json.metadata'
    metadata = my_helper.json_filename + '.json.metadata'
    
    source_dotfile = workdir + '/' + my_helper.my_uuid + '.dot'
    dotfile = my_helper.my_uuid + '.dot'

    source_png = workdir + '/' + my_helper.my_uuid + '.png'
    pngfile = my_helper.my_uuid + '.png'
    
    try:
        #print ('source file {}'.format(source_file_name))
        my_helper.upload_blob(bucket_name, source_metadata, metadata)
        my_helper.upload_blob(bucket_name, source_dotfile, dotfile)
        my_helper.upload_blob(bucket_name, source_png, pngfile)
    except Exception as e:
        print ('Problem uploading data: {}', e)


if __name__ == "__main__":
    main()


"""
__author__     = 'Franklin'
__version__    = '0.1'
__email__      = ''
"""
