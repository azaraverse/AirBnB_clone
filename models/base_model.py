#!/usr/bin/python3
"""BaseModel for AirBnb_clone
"""
import uuid
from datetime import datetime


class BaseModel():
	"""BaseModel class that defines all common attributes/methods
	for other classes.
	"""
	def __init__(self) -> None:
		"""An instance of BaseModel class"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = self.created_at

	def __str__(self) -> str:
		"""Returns a string representation of class.name, id and dict"""
		return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

	def save(self) -> None:
		"""Updates the public instance attribute `updated_at` with
		the current datetime.
		"""
		self.updated_at = datetime.now()

	def to_dict(self) -> dict:
		"""Returns a dictionary containing all keys/values of __dict__
		of the instance.
		"""
		obj_dict = self.__dict__.copy()
		obj_dict['__class__'] = self.__class__.__name__
		obj_dict['created_at'] = self.created_at.isoformat()
		obj_dict['updated_at'] = self.created_at.isoformat()
		return obj_dict
