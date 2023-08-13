#!/usr/bin/python3
"""Will define the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """This represents the BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """This will initialize a new BaseModel

        Args:
            *args (any): unused
            **kwargs (dict): Key/value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for l, w in kwargs.items():
                if l == "created_at" or l == "updated_at":
                    self.__dict__[l] = datetime.strptime(w, tform)
                else:
                    self.__dict__[l] = w
        else:
            models.storage.new(self)

    def save(self):
        """Wil update updated_at with current date and time and save instance"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This will return the dictionary of the BaseModel instance.

        It includes the key/value pair __class__ representing
        the class name of the object
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """This will return the print/str representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

