# Importing the ThunderBase class.
import os
import hashlib
import json
import secrets

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

    def add_record(self, record: dict):
        """Adds a single record to the table."""

        # Getting the schema keys and the record keys for comparison.
        schema_keys = list(self.schema.keys())
        record_keys = list(record.keys())

        schema_length = len(schema_keys)
        counter = 0
        # Checking if all the keys are equal in record and schema.
        while counter < schema_length:
            if schema_keys[counter] != record_keys[counter]:
                return False
            counter += 1

        # Checking if the type of given value in the record matches the prescribed datatype in the schema.
        schema_values = list(self.schema.values())
        record_values = [type(value) for value in record.values()]

        if schema_values != record_values:
            return False

        # Pushing the record into the table as a .tbr file
        record_id = secrets.token_hex(16)
        with open(f'{self.table_path}{record_id}.tbr', 'w') as f:
            record['id'] = record_id
            json.dump(record, f, indent=4)
