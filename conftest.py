import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()