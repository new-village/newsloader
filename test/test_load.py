""" test_load.py
"""
import unittest
from bs4 import BeautifulSoup
from nsloader import WsjAuthentication

class TestResultNkLoader(unittest.TestCase):
    """ Test nsLoader with result arguments
    """
    @classmethod
    def setUpClass(cls):
        # Load normal result case includes suspension entry
        cls.wsj = WsjAuthentication()

    def test_success_case_count(self):
        """ testing success case counts
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = 'https://www.wsj.com/articles/the-fed-absolves-itself-silicon-valley-bank-michael-barr-congress-federal-reserve-failure-2c675ba1'
        res = self.wsj.session.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        self.assertEqual(soup.title.text, "The Fed Failed but Wants More Power - WSJ")

if __name__ == "__main__":
    unittest.main()
