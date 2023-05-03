""" test_load.py
"""
import unittest

from nsloader import test


class TestTestNsLoader(unittest.TestCase):
    """ Test Wall Street Journal's nsLoader
    """
    def test_editorial(self):
        """ testing editorial case
        """
        # Collect and Parse data
        self.assertEqual(test.exec(), 'https://www.wsj.com/')


if __name__ == "__main__":
    unittest.main()
