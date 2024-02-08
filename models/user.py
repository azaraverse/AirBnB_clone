#!/usr/bin/bash/python3
"""
User inheriting from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A User class that inherits from BaseModel."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
