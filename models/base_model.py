#!/usr/bin/python3
"""BaseModel class for AirBnb_clone
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel class that defines all common attributes/methods
    for other classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """An instance of BaseModel class

        Args:
            *args (any): variable arguments.
            **kwargs (any): key-worded arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                            )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns a string representation of class.name, id and dict"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self) -> None:
        """Updates the public instance attribute `updated_at` with
        the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
