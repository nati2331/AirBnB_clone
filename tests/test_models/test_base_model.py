#!/usr/bin/python3
""" Module tests base"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import datetime

class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    my_model = BaseModel()

    def testBaseModel1(self):
        """ Test attributes value of a BaseModel instance """

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.my_model.save()
        self.assertEqual('BaseModel', my_model_json['__class__'])
        my_model_json = self.my_model.to_dict()
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def testSave(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        self.assertIsInstance(self.my_model.id, str)
        self.my_model.first_name = "First"
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.my_model.save()

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])
        self.my_model.save()
        sec_dict = self.my_model.to_dict()
        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])

if __name__ == '__main__':
    unittest.main()

