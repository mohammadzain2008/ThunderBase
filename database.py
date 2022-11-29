# Importing modules
import os
import secrets
import hashlib
import json

# Starting the main class


class ThunderBase:
    """The main class of ThunderBase used for creating a database."""

    def __init__(self, name='root', password='local'):
        """Initializing main attributes of the database."""

        # Declaring the main path variable
        self.path = 'ThunderBase/'

        # Initializing main variables of the database.
        hash = hashlib.sha1(password.encode())

        self.db_name = name
        self.password = hash.hexdigest()
        self.db_id = secrets.token_hex(16)

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
            with open(self.tbdbinfo_path, 'w') as f:
                info_dict = {
                    'id': self.db_id,
                    'name': self.db_name,
                    'password': self.password,
                }
                json.dump(info_dict, f, indent=4)