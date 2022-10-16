#!/usr/bin/python3
"""User module doc"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """class User doc"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
