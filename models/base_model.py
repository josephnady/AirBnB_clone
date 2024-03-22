#!/usr/bin/python3
"""
@author: jozephnady@gmail.com
@file: base_model.py
@time: 2024/02/09
@version: 1.0
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ The base class that all model classes inherit
    id: str
    created_at: datetime
    updated_at: datetime"""

    def __init__(self, *args, **kwargs):
        """constructor of the BaseModel class
        args: Not Used
        Kwargs: Key/Value based keywords"""
        if kwargs:
            edit_kw = kwargs.copy()
            edit_kw['created_at'] = datetime.strptime(
                edit_kw["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            edit_kw['updated_at'] = datetime.strptime(
                edit_kw["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            del edit_kw['__class__']
            self.__dict__.update(edit_kw)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """Return a string representation of the class instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the updated_at attribute and set it with the current time"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = \
                new_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in new_dict:
            new_dict["updated_at"] = \
                new_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
