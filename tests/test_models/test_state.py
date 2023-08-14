#!/usr/bin/python3
""" This will test the State """
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
    """ to check the BaseModel """

    def testpep8(self):
        """ this will test the codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
