"""This module is used for modelling the table of a ThunderBase."""
# pylint score: 9.64/10

# Importing modules
import os
import shutil
import hashlib
import json
import secrets

from database import ThunderBase
import helpers as cf
import tb_errors

# The class for modelling a table.


class Table:
    """This class is used for representing a single table of a ThunderBase."""

    def __init__(self, thunderbase: ThunderBase, schema: dict, name='table'):
        """Initializing and checking main attributes of the table and the parent database."""

        # Checking the passed arguements.

        # Checking if the name of the table is not empty.
        if not name:
            raise tb_errors.TableNameEmpty(
                'The name of the table cannot be null or empty. It must be a string.')

        # Checking if the name of the table is a string or not.
        if not isinstance(name, str):
            raise tb_errors.TableNameInvalid(
                f'The name of the table cannot be of type {type(name)}. It must be a string.')

        # Check if the ThunderBase exists.
        if not cf.is_thunder_base(thunderbase):
            raise tb_errors.ThunderBaseNotFound('ThunderBase not found!')

        # Checking if the schema is empty or not.
        if not schema:
            raise tb_errors.TableSchemaEmpty(
                'The schema of a table cannot be null or empty.' 
                'It must have atleast one key-value pair.')

        # Checking if the schema is a dict or not.
        if not isinstance(schema, dict):
            raise tb_errors.TableSchemaInvalid(
                f'Table schema cannot be of type {type(schema)}. It must be of type dict.')
        # Declaring main self variables
        self.thunderbase = thunderbase
        self.schema = schema
        self.name = name

        hashed_password = hashlib.sha1(self.name.encode())
        hex_digest = hashed_password.hexdigest()

        self.db_dir = self.thunderbase.dirpath
        self.table_path = f"{self.db_dir}{self.name}+{hex_digest}/"

        # Checking if the table already exists.
        if not os.path.exists(self.table_path):
            os.mkdir(self.table_path)

        self.info_file_path = self.table_path + 'INFO.tbtableinfo'

        # Checking if the info file exists.
        if not os.path.exists(self.info_file_path):
            with open(self.info_file_path, 'w', encoding='utf-8'):
                info_dict = {
                    "name": self.name,
                    "schema": self.schema,
                    "database": self.thunderbase.dirname,
                }
                cf.write_info(self.info_file_path, info_dict)

    def truncate(self):
        """Truncates the table including all the records except the info file."""
        table_directory = self.table_path
        for filename in os.listdir(table_directory):
            if filename == 'INFO.tbtableinfo':
                continue
            file_path = os.path.join(table_directory, filename)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def delete(self):
        """Deletes the table."""
        db_directory = self.table_path
        shutil.rmtree(db_directory)

    def add_record(self, record: dict):
        """Adds a single record to the table."""

        # Checking the given record.
        if not record:
            raise tb_errors.TableRecordEmpty(
                'The passed record cannot be null or empty.' 
                'It must contain atleast one key-value pair.')
        # Checking if the record is a dictionary or not.
        if not isinstance(record, dict):
            raise tb_errors.TableRecordInvalid(
                f'A record cannot be of type {type(record)}. It must be a dict.')

        # Getting the schema keys and the record keys for comparison.
        schema_keys = list(self.schema.keys())
        record_keys = list(record.keys())

        schema_length = len(schema_keys)
        record_length = len(record_keys)

        # Checking if the number of keys in both the lists are equal
        if schema_length != record_length:
            raise tb_errors.RecordFieldsIncorrect(
                f'The number of keys in record ({record_length})' 
                f'does not match the number of keys in the table schema ({schema_length})!')

        # Checking if all the keys are equal in record and schema.
        counter = 0
        while counter < schema_length:
            if schema_keys[counter] != record_keys[counter]:
                raise tb_errors.RecordFieldsIncorrect(
                    f'The record should contain the keys ({schema_keys})' 
                    f'but contains the keys ({record_keys})')
            counter += 1

        # Check if type of the value in record matches the given datatype in schema.
        schema_values = list(self.schema.values())
        record_values = [type(value) for value in record.values()]

        if schema_values != record_values:
            raise tb_errors.RecordFieldNotOfSpecifiedType(
                f'The record field[s] do not match the datatype ({record_values})' 
                f'as defined in the corresponding key in the table schema ({schema_values}). ')

        # Pushing the record into the table as a .tbr file
        record_id = secrets.token_hex(16)
        with open(f'{self.table_path}{record_id}.tbr', 'w', encoding='utf-8') as file_object:
            record['id'] = record_id
            json.dump(record, file_object, indent=4)
            return record['id']

    # Functions for deleting a record based on a given value.
    def delete_record_by_id(self, record_id: str):
        """Deletes a record based on the given record id."""

        # Checking if the record exists in directory.
        record_path = f"{self.table_path}{record_id}.tbr"
        if os.path.exists(record_path):
            os.remove(record_path)
            return True
        return False

    def delete_records_by_fields(self, field: dict):
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
            raise tb_errors.TableNotFound(
                'The table associated with the method does not exist!')

        # Looping through every record and skipping the info file.
        for record_name in os.listdir(directory):
            if record_name == 'INFO.tbtableinfo':
                continue

            record_path = os.path.join(directory, record_name)

            # Opening the file and checking if key-value pairs match the given dictionary.
            with open(record_path, encoding='utf-8') as file_object:
                tbr_data = json.load(file_object)

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

    # Functions for searching a record based on a given value.
    def search_record_by_id(self, record_id: str):
        """Returns a record based on the given record id."""

        # Checking if the record exists in directory.
        record_path = f"{self.table_path}{record_id}.tbr"
        if os.path.exists(record_path):
            with open(record_path, encoding='utf-8') as file_object:
                record = json.load(file_object)
            return record
        return False

    def search_records_by_fields(self, field: dict):
        """Returns a single or many records based on the values provided in the given dictionary."""

        # A list for stroring the name[s] of deleted records.
        returned_records = []

        # Extracting the key[s] and value[s] provided.
        keys = []
        values = []
        for key, value in field.items():
            keys.append(key)
            values.append(value)

        # Scanning all the files in the record directory
        directory = self.table_path
        if not os.path.exists(directory):
            raise tb_errors.TableNotFound(
                'The table associated with the method does not exist!')

        # Looping through every record and skipping the info file.
        for record_name in os.listdir(directory):
            if record_name == 'INFO.tbtableinfo':
                continue

            record_path = os.path.join(directory, record_name)

            # Opening the file and checking if key-value pairs match the given dictionary.
            with open(record_path, encoding='utf-8') as file_object:
                tbr_data = json.load(file_object)

                counter = 0
                ans = True

                while counter < len(keys):
                    if tbr_data[keys[counter]] == values[counter]:
                        ans *= True

                    else:
                        ans *= False

                    counter += 1

            # Appending the record file if ans evaluates to true.
            if ans:
                returned_records.append(tbr_data)

        # Returning the list of matching records.
        return returned_records
