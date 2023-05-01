""" test_load.py
"""
import unittest

from bs4 import BeautifulSoup

from nsloader import wsj


class TestResultNkLoader(unittest.TestCase):
    """ Test nsLoader with result arguments
    """
    @classmethod
    def setUpClass(cls):
        # Load normal result case includes suspension entry
        cls.article = wsj.Article()

    def test_success_case(self):
        """ testing success case
        """
        url = 'https://www.wsj.com/articles/the-fed-absolves-itself-silicon-valley-bank-michael-barr-congress-federal-reserve-failure-2c675ba1'
        self.article.load(url)
        self.assertEqual(self.article.title, "The Fed Failed but Wants More Power - WSJ")


if __name__ == "__main__":
    unittest.main()