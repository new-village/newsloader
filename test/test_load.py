""" test_load.py
"""
import unittest
import nsloader

class TestResultNkLoader(unittest.TestCase):
    """ Test nsLoader with result arguments
    """
    @classmethod
    def setUpClass(cls):
        # Load normal result case includes suspension entry
        cls.success = nsloader.load()

    def test_success_case_count(self):
        """ testing success case counts
        """
        self.assertEqual(self.success.title, "title")
        self.assertEqual(self.success.body, "body")
