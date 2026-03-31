import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from selenium.webdriver.common.by import By


class PlannerLoginPage:

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_PASSWORD = (By.XPATH, "//p[text()='Forgot password?']")
    REGISTER_BTN = (By.XPATH, "//button[text()='Register']")
    BUSINESS_LOGIN_BTN = (By.XPATH, "//p[contains(text(),'Own a business')]//button")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*self.SIGN_IN_BTN).click()

    def login(self, email, password):
        self.enter_email(email)
        

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD).click()

    def click_register(self):
        self.driver.find_element(*self.REGISTER_BTN).click()

    def click_business_login(self):
        self.driver.find_element(*self.BUSINESS_LOGIN_BTN).click()
