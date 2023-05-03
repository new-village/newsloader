""" test.py
"""
import logging
 



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_binary

def exec():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    url = 'https://www.wsj.com/'
    driver.get(url)
    logging.info(f'== Success to %s ==' % url)
    # driver.save_screenshot('screenshot.png')
    driver.close()
    driver.quit()

    return url
