""" load.py
"""
import os

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def auth_session(username=None, password=None):
    """ Create authenticated session of the Wall Street Journal by the Requests object.
    :param username: registrated user name or email address
    :param password: registrated password
    :return: :class:`requests.sessions.Session` object
    """
    # Set Parameters
    usr = os.environ['WSJ_USERNAME'] if os.environ['WSJ_USERNAME'] else username
    pwd = os.environ['WSJ_PASSWORD'] if os.environ['WSJ_PASSWORD'] else password

    # passing session info to requests object
    session = requests.session()
    for cookie in _login(usr, pwd):
        session.cookies.set(cookie["name"], cookie["value"])

    # Add header info
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    session.headers.update(headers)

    return session

def _login(username, password) -> list:
    """ Get authenticated session info of the Wall Street Journal.
    :param username: registrated user name or email address
    :param password: registrated password
    :return: List object
    """
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
        # Go to Sign-in page
        driver.find_element(By.LINK_TEXT, "Sign In").click()
        # Login Site
        page1 = [username, '//*[@id="username"]', '//*[@id="basic-login"]/div[1]/form/div[2]/div[6]/div[1]/button[2]']
        page2 = [password, '//*[@id="password-login-password"]', '//*[@id="password-login"]/div/form/div/div[5]/div[1]/button']
        for i in [page1, page2]:
            wait.until(EC.element_to_be_clickable((By.XPATH, i[1]))).send_keys(i[0])
            wait.until(EC.element_to_be_clickable((By.XPATH, i[2]))).click()
        wait.until(EC.title_contains("The Wall Street Journal"))
        # Get cookie
        cookie = driver.get_cookies()
        #driver.save_screenshot('screenshot.png')
    except TimeoutException:
        print("Timeout: Username or Password input failed. Check your credentials.")
    finally:
        # Close firefox
        driver.close()
        driver.quit()
    return cookie
