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
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ dict_json = {}
        for i, j in FileStorage.__objects.items():
            dict_json[i] = j.to_dict() """
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(FileStorage.__objects, default=str))

    def reload(self):
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    json_dict = json.load(f)
                    for i, j in json_dict.items():
                        items = eval(j["__class__"])(**j)
                        FileStorage.__objects[i] = items
        except FileNotFoundError:
            pass
