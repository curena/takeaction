import unittest
import os

class test_environmentVariables(unittest.TestCase):
    def test_APIKey(self):
        self.assertIsNotNone(os.environ.get("SECRET_KEY"))