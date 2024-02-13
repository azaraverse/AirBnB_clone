#!/usr/bin/python3
"""Unittests for filestorage."""
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for filestorage
    """
    def test_file_path(self):
        """Test the file path attribute"""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")


if __name__ == "__main__":
    unittest.main()
