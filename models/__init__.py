#!/usr/bin/python3
"""creates a unique instance of the storage model"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
