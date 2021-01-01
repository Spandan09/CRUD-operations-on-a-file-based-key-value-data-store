# Import python functionalities
import json
import os
import sys
import time
from threading import Lock


# Import custom functionalities created for raising exceptions
from exceptions import *

# GLobal values
file_size = 1024 * 1024 * 1024      # 1 Gb for size of the file
value_size = 16 * 1024 * 1024       # 16 Kb for size of the JSON object


class dataStore:

    def __init__(self, file_path=None):

        self.file_path = file_path

        # Using thread locking property which enables us to perform multithreading
        self.fLock = Lock()     # File lock
        self.dLock = Lock()     # Value Lock

        if file_path:

            if not os.access(file_path, os.F_OK):
                raise FileNotFound

            elif not os.access(file_path, os.R_OK):
                raise FileNotAccessible

            try:
                with open(file_path):
                    pass
            except IOError:
                raise IOErrorOccurred

        # Creates a database in our working directory named db.json
        else:
            self.file_path = os.getcwd() + '/db.json'

        try:

            with open(self.file_path, 'r') as file:

                fileContent = json.load(file)
                self.data = fileContent

                print("Database opened in user's directory i.e.", self.file_path)

        except:

            with open(self.file_path, 'w') as file:

                self.data = dict()
                self.time_to_live = dict()

                print("Database created in user's directory i.e.", self.file_path)

    def validateKey(self, key):

        if type(key) == str:

            if len(key) > 32:
                raise KeyLengthExceeded
            else:
                return True

        else:
            raise InvalidKey

        return False

    def create(self, key='', value='', time_to_live=None):

        self.validateKey(key)

        if key is '':
            raise KeyNotProvided(key)
        if value is '':
            value = None

        with self.fLock:
            if os.path.getsize(self.file_path) > file_size:
                raise FileSizeExceeded

        if sys.getsizeof(value) > value_size:
            raise ValueSizeExceeded

        with self.dLock:

            if key in self.data.keys():
                raise DuplicateKey(key)

            if time_to_live is not None:

                if type(time_to_live) is not int:
                    raise timeToLiveValueError

                time_to_live = int(time.time()) + abs(int(time_to_live))

            temp = {'value': value, 'time_to_live': time_to_live}
            self.data[key] = temp

            with self.fLock:
                json.dump(self.data, fp=open(self.file_path, 'w'), indent=0)

        print("Data created in database")

    def read(self, key=''):

        self.validateKey(key)

        if os.path.getsize(self.file_path) == 0:
            raise EmptyFile

        if key is '':
            raise KeyNotProvided(key)

        with self.dLock:

            if key not in self.data.keys():
                raise KeyNotExist(key)

            time_to_live = self.data[key]['time_to_live']

            if not time_to_live:
                time_to_live = 0

            if time.time() < time_to_live or time_to_live == 0:
                print(key, ":", self.data[key]['value'], "\n")

            else:
                raise KeyExpired(key)

    def update(self, key='', new_value=''):

        self.validateKey(key)

        if os.path.getsize(self.file_path) == 0:
            raise EmptyFile

        if key is '':
            raise KeyNotProvided(key)

        if new_value is '':
            new_value = None

        with self.dLock:

            if key not in self.data.keys():
                raise KeyNotExist(key)

            time_to_live = self.data[key]['time_to_live']

            if not time_to_live:
                time_to_live = 0

            if time.time() < time_to_live or time_to_live == 0:

                print("Original Record:", key, ":",
                      self.data[key]['value'], "\n")

                self.data[key]['value'] = new_value

                print("Value associated with key value", key, "is updated. \n")
                print("Updated record:", key, ":", self.data[key]['value'])

            else:
                raise KeyExpired(key)

    def delete(self, key=''):

        self.validateKey(key)

        if os.path.getsize(self.file_path) == 0:
            raise EmptyFile

        if key == '':
            raise KeyNotProvided(key)

        with self.dLock:

            if key not in self.data.keys():
                raise KeyNotExist(key)

            time_to_live = self.data[key]['time_to_live']

            if not time_to_live:
                time_to_live = 0

            if time.time() < time_to_live or time_to_live == 0:

                self.data.pop(key)

                with self.fLock:

                    file = open(self.file_path, 'w')
                    json.dump(self.data, file)

                print("Data associated with key value", key, "is deleted \n")

                return

            else:
                raise KeyExpired(key)
