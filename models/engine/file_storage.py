#!/usr/bin/python3


import json
from models.base_model import BaseModel
import os.path

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ new_dict = {}

        for i in self.__objects:
            new_dict[i] = self.__objects[i].to_dict() """
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects, default=str))

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                 json_dict = json.loads(f.read())

        except FileNotFoundError:
            pass
