# -*- coding:utf-8 -*-
from seleniumwire import webdriver

from fb_graphql_scraper.drivers.chrome_driver import ChromeDriver
# from fb_graphql_scraper.drivers.firefox_driver import FirefoxDriver # feature
# from fb_graphql_scraper.drivers.edge_driver import EdgeDriver # feature
from fb_graphql_scraper.utils.exceptions import DriverTypeNotSupportException


class DriverFactory(object):

    @classmethod
    def get_driver(cls, driver_type: str, driver_path: str) -> webdriver:
        driver_type = driver_type.lower()

        if driver_type == "chrome":
            return ChromeDriver(driver_path)
        # elif driver_type == "firefox":
        #     return firefox_driver(driver_path)
        # elif driver_type == "edge":
        #     return edge_driver(driver_path)

        raise DriverTypeNotSupportException(driver_type)
