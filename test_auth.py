import unittest
from backend.auth import validate_license
class TestAuth(unittest.TestCase):
    def test_license(self):
        self.assertTrue(validate_license('test', 'hashed_test'))
