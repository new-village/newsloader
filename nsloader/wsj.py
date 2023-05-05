""" wsj.py
"""
import os
from playwright.sync_api import sync_playwright

class Article():
    """ Article class
    """
    def __init__(self, username=None, password=None):
        # Initialize playwright
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
        # Get Environment Parameters
        _usr = os.environ['WSJ_USERNAME'] if os.environ.get('WSJ_USERNAME') else username
        _pwd = os.environ['WSJ_PASSWORD'] if os.environ.get('WSJ_PASSWORD') else password
        # Login the Wall Street Journal
        self._login(_usr, _pwd)
        # Initialize return value
        self.url = None
        self.title = None
        self.sub_title = None
        self.news_outlet = "Wall Street Journal"
        self.date_published = None
        self.authors = None
        self.profile = None
        self.body = None

    def __del__(self):
        self.browser.close()
        self.playwright.stop()

    def _login(self, username, password):
        """ Get authenticated session info of the Wall Street Journal.
        :param username: registrated user name or email address
        :param password: registrated password
        """
        # Access to sign in page
        url = 'https://accounts.wsj.com/login'
        self.page.goto(url, timeout=0)
        # Sign In Page 1
        self.page.locator('input#username').fill(username)
        self.page.locator('span[data-token="continuewithpassword"]').click()
        # Sign In Page 2
        self.page.locator('input#password-login-password').fill(password)
        self.page.get_by_role("button", name="Sign In").click()
        self.page.wait_for_url('https://www.wsj.com/')

    def load(self, url):
        """ load target web site
        """
        self.page.goto(url, timeout=0)

        self.url = url
        self.title = self._extract('h1[class*="StyledHeadline"]')
        self.sub_title = self._extract('h2[class*="Dek-Dek"]')
        self.date_published = self._extract('time[class*="Timestamp-Timestamp"]',"datetime")
        self.authors = self._extract('span[class*="AuthorContainer"]')
        self.profile = self._extract('p[data-type="paragraph"] > em[data-type="emphasis"]')
        # Extract body
        body = [i.text_content() for i in self.page.query_selector_all('p[data-type="paragraph"]')]
        # if there is a profile, delete profile from the document
        if len(self.profile) > 0:
            body.remove(self.profile)
        self.body = '\n'.join(body)

    def _extract(self, selector, extract_attribute=None) -> list:
        target = self.page.query_selector_all(selector)
        if extract_attribute is None:
            contents = ", ".join([i.text_content() for i in target] if len(target) > 0 else list())
        else:
            contents = ", ".join([i.get_attribute(extract_attribute) for i in target] if len(target) > 0 else list())
        return contents

    def to_dict(self) -> dict:
        return {
            'url': self.url,
            'title': self.title,
            'sub_title': self.sub_title,
            'news_outlet': self.news_outlet,
            'date_published': self.date_published,
            'authors': self.authors,
            'profile': self.profile,
            'body': self.body
        }