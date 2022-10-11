#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = self.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        dict_json = {}
        for i, j in FileStorage.__objects.items():
            dict_json[i] = j.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(dict_json))

    def reload(self):
        __objects
