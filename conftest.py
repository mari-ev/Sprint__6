import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os


@pytest.fixture
def driver():
    driver_dir = os.path.join(os.path.dirname(__file__), "drivers")
    driver_path = os.path.join(driver_dir, "geckodriver.exe")

    service = Service(executable_path=driver_path)
    driver = webdriver.Firefox(service=service)

    yield driver
    driver.quit()
