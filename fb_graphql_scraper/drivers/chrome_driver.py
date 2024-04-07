# -*- coding:utf-8 -*-
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service


class ChromeDriver(object):
    def __init__(self, driver_path):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--headless=new")
        chrome_service = Service(driver_path)
        self.driver = webdriver.Chrome(
            service=chrome_service, options=chrome_options)
        self.driver.maximize_window()
