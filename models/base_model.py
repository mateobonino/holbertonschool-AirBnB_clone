#!/usr/bin/python3


import uuid
from datetime import datetime
import models


class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for i, j in kwargs.items():
                if i == 'created_at' or i == 'updated_at':
                    setattr(self, i, datetime.strptime(j, fmt))
                if i == '__class__':
                    continue
                else:
                    setattr(self, i, j)
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
        dict_repr = {'id': self.id, '__class__': self.__class__.__name__}
        try:
            dict_repr['created_at'] = self.created_at.isoformat()
        except:
            dict_repr['created_at'] = self.created_at
        try:
            dict_repr['updated_at'] = self.updated_at.isoformat()
        except:
            dict_repr['updated_at'] = self.updated_at
        return dict_repr
