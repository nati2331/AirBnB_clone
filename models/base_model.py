#!/usr/bin/python3
"""Defines the BaseModel class, the foundation of the HBnB project."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel of the HBnB project.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The creation timestamp.
        updated_at (datetime): The last update timestamp.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): not used.
            **kwargs (dict): value of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update the current datetime and save to storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            dict: Dictionary containing value representing the instance.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """
            Returns:
                str: String containing information about the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

