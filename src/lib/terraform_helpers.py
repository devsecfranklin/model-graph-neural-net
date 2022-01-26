import re

class TerraformHelpers:
    """
    """
    def check_init(self):
        """See if we are ready.

        - Check for presence of .terrafom.lock.hcl
        - Try a `terraform validate`, should return str("Success! The configuration is valid.")
        """
        pass

    def get_public_cloud(self):
        """Check the provider lines in .terraform.lock.hcl to see which public cloud we are working with.
        """
        pass

