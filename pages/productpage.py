from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage():

    def __init__(self,driver):
        
        self.driver = driver
        self.product = (By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        self.gocart = (By.XPATH,"//a[@class='shopping_cart_link']")

    def addproduct(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.product)).click()

    def gotocart(self):
    
       self.driver.find_element(*self.gocart).click()