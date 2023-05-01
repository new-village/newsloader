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
        cls.session = wsj.auth_session()

    def test_success_case_count(self):
        """ testing success case counts
        """
        url = 'https://www.wsj.com/articles/the-fed-absolves-itself-silicon-valley-bank-michael-barr-congress-federal-reserve-failure-2c675ba1'
        res = self.session.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        self.assertEqual(soup.title.text, "The Fed Failed but Wants More Power - WSJ")


if __name__ == "__main__":
    unittest.main()
