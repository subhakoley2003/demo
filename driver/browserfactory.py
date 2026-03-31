from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time



class Browserfactory:

    def get_driver(self,driver):
        if driver == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)
            return self.driver

        if driver == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Firefox(options=options)
            return self.driver


