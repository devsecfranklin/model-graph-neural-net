import os
import re
import sys
from pathlib import Path

from python_terraform import Terraform


class TerraformHelpers:
    """ """

    t = Terraform(terraform_bin_path="/usr/local/bin/terraform")
    lock_file = ".terraform.lock.hcl"
    state_file = ".terraform/terraform.tfstate"

    def collect_digraph_from_terraform(self):
        """Terraform can output a directed graph.

        Command line examples for png and svg format
        # terraform graph | dot -Tpng > graph.png
        # terraform graph | dot -Tsvg -o graph.svg
        """
        return_code, stdout, stderr = self.t.graph(capture_output=True)  # returns str
        if stderr:
            # print(stderr)  # we could automatically run the init at this point?
            return stderr
        return stdout

    def check_init(self):
        """See if we are ready.

        - Check for presence of .terrafom.lock.hcl
        - Try a `terraform validate`, should return str("Success! The configuration is valid.")
        """
        lock_path = Path(self.lock_file)
        state_path = Path(self.state_file)

        ready = True

        if not lock_path.is_file():
            # print('found lockfile')
            ready = False
        return_code, stdout, stderr = self.t.init()  # missing .terraform.lock.hcl
        if stderr:
            ready = False

        return_code, stdout, stderr = self.t.validate(capture_output=True)

        if stderr:
            ready = False

        if not ready:
            print("Terraform not ready, please check state.")
            sys.exit(1)

    def get_public_cloud(self):
        """Check the provider lines in .terraform.lock.hcl to see which public cloud we are working with."""
        pass
