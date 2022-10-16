#!/usr/bin/python3
"""File Storage Class"""

import json
from models.base_model import BaseModel
import os.path


class FileStorage():
    """Manages the object serialization and deserialization to JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects stored"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new objects"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects to JSON"""
        new_dict = {}
        for i in self.__objects:
            new_dict[i] = self.__objects[i].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(new_dict, default=str))

    def reload(self):
        """Loads a JSON file and recreates the object"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State

        classes_dict = {'BaseModel': BaseModel, 'Amenity': Amenity,
                        'City': City, 'Place': Place, 'Review': Review,
                        'User': User, 'State': State}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                for i, j in json.load(f).items():
                    splitted = str(i).split('.')
                    if splitted[0] in classes_dict.keys():
                        self.__objects[i] = classes_dict[splitted[0]](**j)
        except:
            pass
