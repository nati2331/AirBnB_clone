#!/usr/bin/python3
""" Tests storage file """

from models.user import User
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    def test_isPrivate__file_path_attribute(self):
        self.assertEqual(getattr(self.store, '__file_path', None), None)

    def test_isPrivate__objects_attribute(self):
        self.assertEqual(getattr(self.store, 'objects', None), None)

    def test_isDefined__file_path_at_instantiation(self):
        pass

    def test_isEmpty__objects_at_instantiation(self):
        store1 = FileStorage()
        self.assertTrue(len(store1.all()), 0)

    def test_instantiation(self):
        self.assertTrue(isinstance(self.store, FileStorage))

    def test_correct_obj_key_assignment_in__objects(self):
        objects = self.store.all()
        for obj in objects.keys():
            obj_cls = (obj.split('.'))[0]
            self.assertTrue(obj_cls in self.classes)

    def test_method_all_return_at_instantiation(self):
        store1 = FileStorage()
        self.assertTrue(len(store1.all()), 0)

    def test_method_all_return_with__objects(self):
        self.assertTrue(len(self.store.all()) > 0)
        self.assertTrue(len((self.store.all()).keys()) > 0)

    def test_method_new_affects__objects(self):
        store1 = FileStorage()
        base1 = BaseModel()
        self.assertTrue(f"BaseModel.{base1.id}" in (store1.all()).keys())

    def test_method_save_dumps_to__file_path(self):
        self.store.reload()
        self.assertTrue(len((self.store.all()).keys()) > 0)

    def test_method_save_affects__file_path(self):
        store1 = FileStorage()
        base1 = BaseModel()
        store1.reload()
        self.assertTrue(len(store1.all()) > 0)

    def test_method_reload_checks_for__file_path_existence(self):
        self.store.reload()
        self.assertTrue(True)
        pass

