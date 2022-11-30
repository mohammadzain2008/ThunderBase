# Importing modules
import os
from database import ThunderBase
# A module used for checking certain fields or requirements


def isThunderBase(thunderbase: ThunderBase):
    """Function for checking if a given ThunderBase exists."""

    try:
        if os.path.exists(thunderbase.dirpath):
            return True
    except:
        return False


def writeInfo(filepath, info):
    """Function for writing to a file."""
    with open(filepath, 'w') as f:
        f.write(str(info))
