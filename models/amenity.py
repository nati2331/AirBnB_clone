#!/usr/bin/python3
""" Defines the Amenity class, a subclass of BaseModel. """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

