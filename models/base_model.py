#!/usr/bin/python3
==================
Class BaseModel
=================
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ constructor"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Prints a string"""
        return('[' + type(self).__name__ + '] ('
                + str(self.id) + ') ' + str(self.__dict__))

    def save(self):
        """updates updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
