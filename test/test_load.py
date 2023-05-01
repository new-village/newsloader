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

    def test_title(self):
        """ testing success case
        """
        url = 'https://www.wsj.com/articles/the-fed-absolves-itself-silicon-valley-bank-michael-barr-congress-federal-reserve-failure-2c675ba1'
        self.article.load(url)
        self.assertEqual(self.article.title, "The Fed Failed but Wants More Power")

    def test_date_published(self):
        """ testing success case
        """
        url = 'https://www.wsj.com/articles/dont-count-ron-desantis-out-trump-2024-gop-primary-moderates-culture-war-34be9a75?mod=opinion_lead_pos5'
        self.article.load(url)
        self.assertEqual(self.article.date_published, "2023-04-30T20:47:00Z")

    def test_authors(self):
        """ testing success case
        """
        url = 'https://www.wsj.com/articles/ai-needs-guardrails-and-global-cooperation-chatbot-megasystem-intelligence-f7be3a3c'
        self.article.load(url)
        self.assertEqual(self.article.authors, "Susan Schneider")


if __name__ == "__main__":
    unittest.main()