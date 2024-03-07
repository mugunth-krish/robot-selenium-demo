from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from robot.api import logger


class CustomLib():
    """
    Selenium custom library
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.driver = None

    def open_browser(self, url):
        self.driver = webdriver.Chrome()


    def click_by_id(self, id):


    def send_keys_by_id(self, id, key_to_be_sent):


    def read_text_by_id(self, id):


    def close_browser(self):
        self.driver.close()