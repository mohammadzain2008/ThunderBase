"""A module used for checking certain fields or requirements"""
# pylint score: 10/10

# Importing modules
import os
from database import ThunderBase


def is_thunder_base(thunderbase: ThunderBase):
    """Function for checking if a given ThunderBase exists."""

    if os.path.exists(thunderbase.dirpath):
        return True
    return False


def write_info(filepath, info):
    """Function for writing to a file."""
    with open(filepath, 'w', encoding='utf-8') as file_object:
        file_object.write(str(info))
