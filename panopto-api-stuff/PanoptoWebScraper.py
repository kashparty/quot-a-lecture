from bs4 import BeautifulSoup
import requests
from http.cookiejar import MozillaCookieJar
import webbrowser
import json
from urllib.request import urlopen
from base64 import b64encode
from hashlib import sha256
from lxml import html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

import time

from getpass import getpass

login_url = "https://office.imperial.ac.uk/"

url = "https://imperial.cloud.panopto.eu/Panopto"

url_show250 = "https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#isSharedWithMe=true&maxResults=250"

def main(showBrowser = True):

    chrome_options = Options()
    if not showBrowser:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % "1920, 1080")
    driver = webdriver.Chrome(executable_path="chromedriver97.exe", chrome_options=chrome_options)
    sign_in(driver)
    print(get_video_links(driver))


def get_video_links(driver):
    driver.get(url_show250)
    time.sleep(10)
    return list(map(lambda e: e.get_attribute("href"),
                    driver.find_element_by_id("detailsTable").find_elements_by_class_name("thumbnail-link")))


def sign_in(driver):
    driver.get(login_url)
    time.sleep(3)
    username = driver.find_element_by_id("i0116")
    username.send_keys(input("Enter username: "))
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(3)
    password = driver.find_element_by_id("i0118")
    password.send_keys(getpass("Enter password: "))
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(3)





input("Enter to start")
try:
    main()
except Exception as e:
    print(e)
input("End of program!")




