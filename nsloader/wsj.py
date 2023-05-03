""" load.py
"""
import logging
import os

import chromedriver_binary
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Article():
    def __init__(self, username=None, password=None):
        logging.info('Initialize the Article class')
        self.driver = self._login(username, password)
        self.soup = None
        self.url = None
        self.title = None
        self.sub_title = None
        self.news_outlet = "Wall Street Journal"
        self.date_published = None
        self.authors = None
        self.profile = None
        self.body = None

    def __del__(self):
        self.driver.close()
        self.driver.quit()

    def _login(self, username=None, password=None):
        """ Get authenticated session info of the Wall Street Journal.
        :param username: registrated user name or email address
        :param password: registrated password
        :return: :class: `driver` object
        """
        # Set Parameters
        usr = os.environ['WSJ_USERNAME'] if os.environ['WSJ_USERNAME'] else username
        pwd = os.environ['WSJ_PASSWORD'] if os.environ['WSJ_PASSWORD'] else password
        url = "https://www.wsj.com/"
        # Initialize browser
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        # Create Firefox's webdriver object
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        # Access to initial page
        driver.get(url)
        wait = WebDriverWait(driver=driver, timeout=10)
        try:
            # Go to Sign-in page
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SIGN IN"))).click()
            # Login Site
            page1 = [usr, '//*[@id="username"]', '//*[@id="basic-login"]/div[1]/form/div[2]/div[6]/div[1]/button[2]']
            page2 = [pwd, '//*[@id="password-login-password"]', '//*[@id="password-login"]/div/form/div/div[5]/div[1]/button']
            for i in [page1, page2]:
                wait.until(EC.element_to_be_clickable((By.XPATH, i[1]))).send_keys(i[0])
                wait.until(EC.element_to_be_clickable((By.XPATH, i[2]))).click()
            wait.until(EC.title_contains("The Wall Street Journal"))
            # driver.save_screenshot('screenshot.png')
        except TimeoutException:
            logging.warning("Timeout: Username or Password input failed. Check your credentials.")

        return driver

    def load(self, url):
        # Get HTML and convert soup object
        logging.info(f'Start to collect %s' % url)
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source.encode('utf-8'), 'html.parser')

        # Extract each properties
        self.url = url
        self.title = self._extract('h1[class*="StyledHeadline"]')
        self.sub_title = self._extract('h2[class*="Dek-Dek"]')
        self.date_published = self._extract('time[class*="Timestamp-Timestamp"]',"datetime")
        self.authors = self._extract('span[class*="AuthorContainer"]')
        self.profile = self._extract('p[data-type="paragraph"] > em[data-type="emphasis"]')
        # Extract body
        body = [i.text for i in self.soup.select('p[data-type="paragraph"]')]
        # if there is a profile, delete profile from the document
        if len(self.profile) > 0:
            body.remove(self.profile)
        self.body = '\n'.join(body)

        return self

    def _extract(self, selector, extract_attribute=None) -> list:
        target = self.soup.select(selector)
        if extract_attribute is None:
            contents = ", ".join([i.text for i in target] if len(target) > 0 else list())
        else:
            contents = ", ".join([i[extract_attribute] for i in target] if len(target) > 0 else list())
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