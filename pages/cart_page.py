from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage():
    checkout_btn = (By.ID, "checkout")

    def __init__(self,driver):
        self.driver = driver

    def checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout_btn)).click()