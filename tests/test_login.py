from pages.login_page import Login_page
from pages.productpage import ProductPage
from pages.cart_page import CartPage
from pages.checkoutInformation import CheckoutInformationPage
from pages.checkoutoverview import  CheckoutOverviewPage  


def test_valid_login(setup):
     driver = setup

     lgn = Login_page(driver);
     lgn.login("standard_user","secret_sauce")

     prod = ProductPage(driver)
     prod.addproduct()
     prod.gotocart()

     cart = CartPage(driver)
     cart.checkout()

     checkout_info = CheckoutInformationPage(driver)
     checkout_info.enter_checkout_information("John","Doe","12345")

     checkout_overview = CheckoutOverviewPage(driver)
     checkout_overview.finish_checkout()


    
