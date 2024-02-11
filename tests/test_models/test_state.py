#!/usr/bin/python3
""" tests for the class state """

from models.base_model import BaseModel
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """ Define State attributes and methods tests """

    def test_state_isinstance_of_BaseModel(self):
        """ test that State class inherits from BaseModel """
        self.assertTrue(isinstance(self.state, BaseModel))

    # test that the class correctly instantiates
    def test_state_instantiation(self):
        """ test that State class correctly instantiates """
        self.assertTrue(isinstance(self.state, State))

    def test_state_isStr_name(self):
        """ test that name public attribute is a string """
        self.assertTrue(isinstance(getattr(self.state, 'name', None), str))

    def test_state_isAttribute_name(self):
        """ test that State class contains name public attribute """
        self.assertTrue(getattr(self.state, 'name', None) is not None)

    def test_state_isNotAttribute_nonExistent(self):
        """ test that State class does Not contain public attribute,
        nonExistent """
        self.assertTrue(getattr(self.state, 'nonExistent', None) is None)

    def setUp(self):
        """ Instantiate User test objects """
        self.state = State()

