import os
import sys
import pytest
import configparser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from driver.browserfactory import Browserfactory
from pages.plannerpages.plannerlogin_page import PlannerLoginPage
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger(__name__)

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../../config.ini"))

BASE_URL = config["planner"]["base_url"]
EMAIL = config["planner"]["email"]
PASSWORD = config["planner"]["password"]


@pytest.fixture
def driver():
    logger.info("Launching Chrome browser")
    driver = Browserfactory().get_driver("chrome")
    driver.get(BASE_URL)
    logger.info(f"Navigated to {BASE_URL}")
    yield driver
    driver.quit()
    logger.info("Browser closed")


def test_planner_login(driver):
    try:
        logger.info(f"Logging in with email: {EMAIL}")
        login_page = PlannerLoginPage(driver)
        login_page.login(EMAIL, PASSWORD)
        # take_screenshot(driver, "planner_login_success")
        assert driver.current_url != BASE_URL, "Login failed: URL did not change after sign in"
        logger.info(f"Login successful. Redirected to: {driver.current_url}")
    except Exception as e:
        take_screenshot(driver, "planner_login_failure")
        logger.error(f"Login test failed: {str(e)}")
        raise

