import re
from pathlib import Path

class TerraformHelpers:
    """
    """

    lock_file = '.terraform.lock.hcl'
    state_file = 'terraform.tfstate'
    
    def check_init(self):
        """See if we are ready.

        - Check for presence of .terrafom.lock.hcl
        - Try a `terraform validate`, should return str("Success! The configuration is valid.")
        """
        lock_path = Path(self.lock_file)
        state_path = Path(self.state_file)

        if lock_path.is_file():
            print('found lockfile')

        if state_path.is_file():
            print('found statefile')

    def get_public_cloud(self):
        """Check the provider lines in .terraform.lock.hcl to see which public cloud we are working with.
        """
        pass

