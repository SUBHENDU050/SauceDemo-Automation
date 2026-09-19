from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    finish_button = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    print("Checkout Overview Page loaded successfully.")


    