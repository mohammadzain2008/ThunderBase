# Importing the ThunderBase class.
import os
import hashlib
import json

from database import ThunderBase
import helpers as cf

# The class for modelling a table.


class Table:
    """This class is used for representing a single table of a ThunderBase."""

    def __init__(self, thunderbase: ThunderBase, schema: dict, name='table'):
        """Initializing and checking main attributes of the table and the parent database."""

        # Check if the ThunderBase exists.
        if not cf.isThunderBase(thunderbase):
            return False

        # Declaring main self variables
        self.thunderbase = thunderbase
        self.schema = schema
        self.name = name

        hash = hashlib.sha1(self.name.encode())
        hex_digest = hash.hexdigest()

        self.db_dir = self.thunderbase.dirpath
        self.table_path = f"{self.db_dir}{self.name}+{hex_digest}/"

        # Checking if the table already exists.
        if not os.path.exists(self.table_path):
            os.mkdir(self.table_path)

        self.info_file_path = self.table_path + 'INFO.tbtableinfo'
        # Checking if the info file exists.
        if not os.path.exists(self.info_file_path):
            with open(self.info_file_path, 'w') as f:
                info_dict = {
                    "name": self.name,
                    "schema": self.schema,
                    "database": self.thunderbase.dirname,
                }
                cf.writeInfo(self.info_file_path, info_dict)
