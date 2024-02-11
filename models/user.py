#!/usr/bin/python3
""" Defines class user """
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
