from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

        def __init__(self, driver):
                        
            self.driver = driver
            self.username = (By.ID, "user-name")
            self.password = (By.ID, "password")
            self.login_btn = (By.ID, "login-button")
            self.error_message = (By.XPATH, "//h3[@data-test='error']")
                   
        def login(self, username, password):
            self.driver.find_element(*self.username).send_keys(username)
            self.driver.find_element(*self.password).send_keys(password)
            self.driver.find_element(*self.login_btn).click()
            
        def get_error_message(self):
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.error_message)).text