#!/usr/bin/python3
"""
Testing BaseModel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests our BaseModel class."""

    def setUp(self) -> None:
        """Setup two instantiation models."""
        self.Base1 = BaseModel()
        self.Base2 = BaseModel()

    def test_initialisation(self):
        """Test if BaseModel is not empty on initialisation."""
        self.assertIsNotNone(self.Base1)
        self.assertIsNotNone(self.Base2)

    def test_hasattr_Base1(self):
        """Test if all attributes are in Base1 Model."""
        self.assertTrue(hasattr(self.Base1, 'id'))
        self.assertTrue(hasattr(self.Base1, 'created_at'))
        self.assertTrue(hasattr(self.Base1, 'updated_at'))

    def test_hasattr_Base2(self):
        """Tests if all attributes are in Base2 Model."""
        self.assertTrue(hasattr(self.Base2, 'id'))
        self.assertTrue(hasattr(self.Base2, 'created_at'))
        self.assertTrue(hasattr(self.Base2, 'updated_at'))

    def test_instance_type_created_at(self):
        """Checks type for created at attr."""
        self.assertIsInstance(self.Base1.created_at, datetime)
        self.assertIsInstance(self.Base2.created_at, datetime)

    def test_instance_type_updated_at(self):
        """Checks the type for updated at attr."""
        self.assertIsInstance(self.Base1.updated_at, datetime)
        self.assertIsInstance(self.Base2.updated_at, datetime)

    def test_time_format_Base1_created_at(self):
        """Checks if format of datetime is in ISO format."""
        exp_ISO_format = self.Base1.created_at.isoformat()
        Base1_dict = self.Base1.to_dict()
        self.assertEqual(Base1_dict['created_at'], exp_ISO_format)

    def test_time_format_Base2_created_at(self):
        """Checks if format of datetime is in ISO format."""
        exp_ISO_format = self.Base2.created_at.isoformat()
        Base2_dict = self.Base2.to_dict()
        self.assertEqual(Base2_dict['created_at'], exp_ISO_format)

    def test_time_format_Base1_updated_at(self):
        """Checks if format of datetime is in ISO format."""
        exp_ISO_format = self.Base1.updated_at.isoformat()
        Base1_dict = self.Base1.to_dict()
        self.assertEqual(Base1_dict['updated_at'], exp_ISO_format)

    def test_time_format_Base2_updated_at(self):
        """Checks if format of datetime is in ISO format."""
        exp_ISO_format = self.Base2.updated_at.isoformat()
        Base2_dict = self.Base2.to_dict()
        self.assertEqual(Base2_dict['updated_at'], exp_ISO_format)

    def test_non_empty_id(self):
        """Tests for non empty ID in both models."""
        self.assertNotEqual(self.Base1.id, '')
        self.assertNotEqual(self.Base2.id, '')

    def test_uuid(self):
        """Tests the unique IDs and make sure they do not match."""
        self.assertNotEqual(self.Base1.id, self.Base2.id)

    def test_uuid_type_Base1(self):
        """Tests the type of ID of Base1."""
        self.assertTrue(type(self.Base1.id), str)

    def test_uuid_type_Base2(self):
        """Tests the type of ID of Base2."""
        self.assertTrue(type(self.Base2.id), str)

    def test_variance_between_created_and_updated_at(self):
        """Test the time variance between creation and update time.
        Should be the same when newly created. Test update in save
        method later down.
        """
        self.assertEqual(self.Base1.created_at, self.Base1.updated_at)
        self.assertEqual(self.Base2.created_at, self.Base2.updated_at)

    def test_str_method(self):
        """Test the str method of the BaseModel."""
        string1 = f'[BaseModel] ({self.Base1.id}) {self.Base1.__dict__}'
        self.assertEqual(str(self.Base1), string1)

        string2 = f'[BaseModel] ({self.Base2.id}) {self.Base2.__dict__}'
        self.assertEqual(str(self.Base2), string2)

    def test_str_method_with_attr_Base1(self):
        """Tests the str method with additional attr passed to it."""
        self.Base1.name = 'Betty'
        self.Base1.my_number = 89
        string1 = f'[BaseModel] ({self.Base1.id}) {self.Base1.__dict__}'
        self.assertEqual(str(self.Base1), string1)

    def test_str_method_with_attr_Base2(self):
        """Tests the str method with additional attr passed to it."""
        self.Base2.name = 'FooBar'
        self.Base2.my_number = 98
        string2 = f'[BaseModel] ({self.Base2.id}) {self.Base2.__dict__}'
        self.assertEqual(str(self.Base2), string2)

    def test_save_method_base1(self):
        """Tests the save method on Base1. should be at different times"""
        initial_updated_at = self.Base1.updated_at
        self.Base1.save()
        self.assertNotEqual(initial_updated_at, self.Base1.updated_at)

    def test_save_method_base2(self):
        """Tests the save method on Base1. should be at different times"""
        initial_updated_at = self.Base2.updated_at
        self.Base2.save()
        self.assertNotEqual(initial_updated_at, self.Base2.updated_at)

    def test_to_dict_method_base1(self):
        """Test to_dict method on Base1."""
        base1_dict = self.Base1.to_dict()
        # confirm dict type
        self.assertIsInstance(base1_dict, dict)

        # confirm __class__ key in dictionary
        self.assertIn('__class__', base1_dict)

        # confirm classname is as expected in the dictionary
        self.assertEqual(base1_dict['__class__'], 'BaseModel')

        # further confirm if created_at is in dictionary
        self.assertIn('created_at', base1_dict)

        # finally confirm if updated_at is in dictionary
        self.assertIn('updated_at', base1_dict)

    def test_to_dict_method_base2(self):
        """Test to_dict method on Base2."""
        base2_dict = self.Base2.to_dict()
        # confirm dict type
        self.assertIsInstance(base2_dict, dict)

        # confirm __class__ key in dictionary
        self.assertIn('__class__', base2_dict)

        # confirm classname is as expected in the dictionary
        self.assertEqual(base2_dict['__class__'], 'BaseModel')

        # further confirm if created_at is in dictionary
        self.assertIn('created_at', base2_dict)

        # finally confirm if updated_at is in dictionary
        self.assertIn('updated_at', base2_dict)


if __name__ == '__main__':
    unittest.main()
