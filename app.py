from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import threading

class Browser:
    def __init__(self):
        self.driver = None
        self.last_check = None

        self.reset_driver_minutes = 15
        self.close_driver_minutes = 10

        self.last_use = datetime.now()

        self.manage_thread = threading.Thread(target=self.loop, args=())
        self.manage_thread.start()

    def check_driver(self):

        self.last_use = datetime.now()
        self.last_check = datetime.now()

        if self.driver == None or (datetime.now() - self.last_check).total_seconds() > self.reset_driver_minutes * 60:
            self.driver = webdriver.Chrome()
            print("...Driver opened")
            return
    def loop(self):
        while True:
            time.sleep(1)
            print(self.close_driver_minutes * 60)
            if (datetime.now() - self.last_use).total_seconds() >= self.close_driver_minutes * 60 and self.driver != None:
                self.driver.close()
                self.driver = None
                print("...Driver closed")

    def open(self, url):
        self.check_driver()
        self.driver.get(url)

    def get_element(self, by_selector, search_str, desired_component):
        selector = getattr(By, by_selector)
        element = self.driver.find_element(selector, search_str)

        return getattr(element, desired_component)
b = Browser()

b.open("https://www.google.com")
c = b.get_element("CSS_SELECTOR", "body", "text")
print(c)