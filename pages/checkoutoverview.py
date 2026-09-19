from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    finish_button = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

print("Checkout Overview Page loaded successfully.")


    