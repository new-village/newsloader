""" test_load.py
"""
import random
import time
import unittest

from nsloader import wsj


class TestWsjNsLoader(unittest.TestCase):
    """ Test Wall Street Journal's nsLoader
    """
    @classmethod
    def setUpClass(cls):
        # Load normal result case includes suspension entry
        cls.article = wsj.Article()

    def test_editorial(self):
        """ testing editorial case
        """
        # Expected result data
        expect = {
            "url": "https://www.wsj.com/articles/the-fed-absolves-itself-silicon-valley-bank-michael-barr-congress-federal-reserve-failure-2c675ba1",
            "title": "The Fed Failed but Wants More Power",
            "sub_title": "As expected, Michael Barr blames Congress and his predecessor for Silicon Valley Bank’s failure.",
            "news_outlet": "Wall Street Journal",
            "date_published": "2023-04-30T21:38:00Z",
            "authors": "The Editorial Board",
            "profile": 0,
            "body": 4199
        }

        # Collect and Parse data
        self.article.load(expect['url'])
        time.sleep(random.randrange(5))

        # Contents Masking
        result = self.article.to_dict()
        for key in ["profile", "body"]:
            result[key] = len(result[key])
        self.assertDictEqual(result, expect)


    def test_commentary(self):
        """ testing commentary case
        """
        # Expected result data
        expect = {
            "url": "https://www.wsj.com/articles/ai-needs-guardrails-and-global-cooperation-chatbot-megasystem-intelligence-f7be3a3c",
            "title": "Artificial Intelligence Needs Guardrails and Global Cooperation",
            "sub_title": "Risks abound when the internet becomes a playpen for thousands, perhaps millions, of artificial intelligence systems.",
            "news_outlet": "Wall Street Journal",
            "date_published": "2023-04-28T21:05:00Z",
            "authors": "Susan Schneider, Kyle Kilian",
            "profile": 275,
            "body": 9246
        }

        # Collect and Parse data
        self.article.load(expect['url'])
        time.sleep(random.randrange(5))

        # Contents Masking
        result = self.article.to_dict()
        for key in ["profile", "body"]:
            result[key] = len(result[key])
        self.assertDictEqual(result, expect)


if __name__ == "__main__":
    unittest.main()