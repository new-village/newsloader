""" test.py
"""
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

def exec():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    url = 'https://www.wsj.com/'
    driver.get(url)
    logging.info(f'== Success to %s ==' % url)
    driver.save_screenshot('screenshot.png')
    driver.close()
    driver.quit()

    return url
