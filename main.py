#!/usr/bin/python3

from models.base_model import BaseModel


model = BaseModel()

print(model.id)
print(model.updated_at)
print(model.created_at)
print(model.__str__())
print()
print(model.to_dict())