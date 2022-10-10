#!/usr/bin/python3


import uuid
import datetime


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'created_at':
                    self.created_at = j.isoformat()
                if i == 'updated_at':
                    self.updated_at = j.isoformat()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_repr = {'id': self.id, 
                    'created_at': self.created_at.isoformat(), 
                    'updated_at': self.updated_at.isoformat(), 
                    '__class__': self.__class__.__name__}
        return dict_repr
