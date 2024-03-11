#!/usr/bin/env python3
"""This is a module for file storage class.
The class is used to serializes instances to a JSON file
and deserializes JSON file to instances"""


import json


class FileStorage:
    """This class is used to serializes instances to a JSON
    file and deserializes JSON file to instances"""

    __file_path = "data.json"
    __objects = {}

    def all(self):
        """This method returns all the dictionary data in __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets in an object in __objects
        with the key <obj class name>.id

        Args:
            obj - this argument is the object (new object) that
            is to be stored in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """This method serializes the objects in __objects to the JSON
        format and save them in the file, specified by __file_path"""
        with open(FileStorage.__file_path, 'w', encoding='utf8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """This method deserializes the JSON file content to __objects,
        only if the JSON file exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf8') as f:
                FileStorage.__objects = json.load(f)
        except Exception as e:
            pass

    @staticmethod
    def reset_objects():
        """This method resets the number of object to zero.
        It is meant for only unittest usage"""
        FileStorage.__objects = {}
