#!/usr/bin/python3
"""Review module doc"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review doc"""
    place_id = ""
    user_id = ""
    text = ""
