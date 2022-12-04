"""The module which contains the class for creating a ThunderBase."""
# pylint score: 9.77/10

# Importing modules
import os
import shutil
import hashlib
import json

import tb_errors
# Starting the main class


class ThunderBase:
    """The main class of ThunderBase used for creating a database."""

    def __init__(self, name='root', password='local'):
        """Initializing main attributes of the database."""

        # Adding checks to the arguements passed

        # Checking the name.
        if not name:
            raise tb_errors.ThunderBaseNameEmpty(
                'The name of the ThunderBase cannot be null or an empty string.')

        if not isinstance(name, str):
            raise tb_errors.ThunderBaseInvalidName(
                f'The name of the ThunderBase cannot be of type {type(name)}. It must be a string.')

        # Checking the password.
        if not password:
            raise tb_errors.ThunderBasePasswordEmpty(
                'The password of the ThunderBase cannot be null or an empty string.')

        if not isinstance(password, str):
            raise tb_errors.ThunderBaseInvalidPassword(
                f'The password of the ThunderBase cannot be of type {type(password)}.' 
                'It mush be a string.')

        # Declaring the main path variable
        self.path = 'ThunderBase/'

        # Initializing main variables of the database.
        hashed_password = hashlib.sha1(password.encode())

        self.db_name = name
        self.password = hashed_password.hexdigest()

        # Creating the directory name for the database.
        self.dirname = f"{self.db_name}+{self.password}/"
        self.dirpath = self.path + self.dirname

        # Creating the ThunderBase directory.
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        # Make the associative folder of the database into the respected folder.
        if not os.path.exists(self.dirpath):
            os.mkdir(self.dirpath)

        # Make the main .tbdbinfo file for the database
        self.tbdbinfo_path = self.dirpath + 'INFO.tbdbinfo'

        if not os.path.exists(self.tbdbinfo_path):
            with open(self.tbdbinfo_path, 'w', encoding='utf-8') as file_object:
                info_dict = {
                    'name': self.db_name,
                    'password': self.password,
                }
                json.dump(info_dict, file_object, indent=4)

    def truncate(self):
        """Truncates all the contents of a database except the info file."""
        db_directory = self.dirpath
        for filename in os.listdir(db_directory):
            if filename == 'INFO.tbdbinfo':
                continue
            file_path = os.path.join(db_directory, filename)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def delete(self):
        """Deletes the ThunderBase."""
        db_directory = self.dirpath
        shutil.rmtree(db_directory)
