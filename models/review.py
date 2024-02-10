#!/usr/bin/python3
"""
Review class inheriting from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review Class that inherits from BaseModel."""
    place_id = ''
    user_id = ''
    text = ''
