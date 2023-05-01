""" load.py
"""
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WsjAuthentication():
    """ Wall Street Journal Authentication
    """
    def __init__(self, username=None, password=None):
        _usr = os.environ['WSJ_USERNAME'] if os.environ['WSJ_USERNAME'] else username
        _pwd = os.environ['WSJ_PASSWORD'] if os.environ['WSJ_PASSWORD'] else password
        self.session = self._login(_usr, _pwd)

    def __repr__(self):
        return self.session

    def _login(self, username, password):
        url = "https://www.wsj.com/"

        # Initialize browser
        options = Options()
        options.add_argument('--headless')
        # Create Firefox's webdriver object
        driver = webdriver.Firefox(options=options)
        # Access to initial page
        driver.get(url)
        wait = WebDriverWait(driver=driver, timeout=10)

        try:
            # Open Sign In Page
            driver.find_element(By.LINK_TEXT, "Sign In").click()
            # Login Site
            page1 = [username, '//*[@id="username"]', '//*[@id="basic-login"]/div[1]/form/div[2]/div[6]/div[1]/button[2]']
            page2 = [password, '//*[@id="password-login-password"]', '//*[@id="password-login"]/div/form/div/div[5]/div[1]/button']
            for i in [page1, page2]:
                wait.until(EC.element_to_be_clickable((By.XPATH, i[1]))).send_keys(i[0])
                wait.until(EC.element_to_be_clickable((By.XPATH, i[2]))).click()
            wait.until(EC.title_contains("The Wall Street Journal"))
            #driver.save_screenshot('screenshot.png')
        except TimeoutException:
            print("Timeout: Username or Password input failed. Check your credentials.")
        finally:
            # passing session info to requests object
            _sess = requests.session()
            for cookie in driver.get_cookies():
                _sess.cookies.set(cookie["name"], cookie["value"])
            # Close firefox
            driver.close()
            driver.quit()
        return _sess
