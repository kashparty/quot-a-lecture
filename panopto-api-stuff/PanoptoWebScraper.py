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

url_template = "https://{0}/Panopto"


def main(show_browser=True):
    domain = input("Enter Panopto domain (e.g: imperial.cloud.panopto.eu): ")
    chrome_options = Options()
    if not show_browser:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % "1920, 1080")
    driver = webdriver.Chrome(executable_path="chromedriver97.exe", chrome_options=chrome_options)
    sign_in(driver, domain)
    print("Downloading lecture transcripts...")
    for vid_url in get_video_links(driver, domain):
        save_transcript(driver, vid_url)


def save_transcript(driver, video_url):
    driver.get(video_url)
    time.sleep(5)
    folder = driver.find_element_by_id("parentName").text
    driver.find_element_by_id("detailsTabHeader").click()
    time.sleep(1)
    lecturer = driver.find_element_by_id("detailsTab").find_element_by_class_name("owner").text.split('\n')[1]
    driver.find_element_by_id("transcriptTabHeader").click()
    time.sleep(1)
    captions = driver.find_element_by_id("transcriptTabPane").find_element_by_class_name(
        "event-tab-list").find_elements_by_class_name("index-event ")
    title = driver.find_element_by_id("deliveryTitle").text
    print("Downloading transcript from: " + title)
    print("There are: " + str(len(captions)) + " caption lines.")
    transcript = "Category: {0}\nLecturer: {1}\n".format(folder, lecturer) + "\n".join(
        map(lambda e: e.find_element_by_class_name("event-text").find_element_by_tag_name(
            "span").text + "\n" + e.find_element_by_class_name("event-time").text, captions))
    file = open(title + ".txt", "w")
    file.write(transcript)
    file.close()
    print("Saved to " + title + ".txt")


def get_video_links(driver, domain):
    driver.get("https://{0}/Panopto".format(domain))
    time.sleep(10)
    return list(map(lambda e: e.get_attribute("href"),
                    driver.find_element_by_id("detailsTable").find_elements_by_class_name("thumbnail-link")))


def sign_in(driver, domain):
    driver.get("https://{0}/Panopto".format(domain))
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
    main(show_browser=False)
except Exception as error:
    print(error)
input("End of program!")
