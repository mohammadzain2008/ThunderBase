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
            return record['id']

    # Functions for deleting a record based on a given value.
    def delete_record_by_id(self, id: str):
        """Deletes a record based on the given record id."""

        # Checking if the record exists in directory.
        record_path = f"{self.table_path}{id}.tbr"
        if os.path.exists(record_path):
            os.remove(record_path)
            return True
        else:
            return False

    def delete_records_by_field(self, field: dict):
        """Deletes a single or many records based on the values provided in the given dictionary."""

        # A list for stroring the name[s] of deleted records.
        deleted_records = []

        # Extracting the key[s] and value[s] provided.
        keys = []
        values = []
        for key, value in field.items():
            keys.append(key)
            values.append(value)

        # Scanning all the files in the record directory
        directory = self.table_path
        if not os.path.exists(directory):
            print("NO DIR")
            return False

        # Looping through every record and skipping the info file.
        for record_name in os.listdir(directory):
            if record_name == 'INFO.tbtableinfo':
                continue

            record_path = os.path.join(directory, record_name)

            # Opening the file and checking if key-value pairs match the given dictionary.
            with open(record_path) as f:
                tbr_data = json.load(f)

                counter = 0
                ans = True

                while counter < len(keys):
                    if tbr_data[keys[counter]] == values[counter]:
                        ans *= True

                    else:
                        ans *= False

                    counter += 1

            # Removing the record file if ans evaluates to true.
            if ans:
                os.remove(record_path)
                deleted_records.append(record_path)

        # Returning the list of deleted records.
        return deleted_records