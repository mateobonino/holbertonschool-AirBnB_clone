#!/usr/bin/python3


import uuid
from datetime import datetime
import models


class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for i, j in kwargs.items():
                if i == 'created_at':
                    self.created_at = datetime.fromisoformat(j)
                if i == 'updated_at':
                    self.updated_at = datetime.fromisoformat(j)
                if i == '__class__':
                    continue
                if i == 'id':
                    self.id = j
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        dict_repr['__class__'] = self.__class__.__name__
        return dict_repr
