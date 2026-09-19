import pytest
from pages.login_page import LoginPage
from pages.productpage import ProductPage
from pages.cart_page import CartPage
from pages.checkoutInformation import CheckoutInformationPage
from pages.checkoutoverview import CheckoutOverviewPage


login_data = [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("wrong_user", "wrong_pass", False),
    ("", "", False),
]


@pytest.mark.parametrize("username,password,expected_success", login_data)

def test_login_data_driven(setup, username, password, expected_success):
    driver = setup

    lgn = LoginPage(driver)
    lgn.login(username, password) 

    if expected_success:
        
        prod = ProductPage(driver)
        app_log = prod.logo_displayed()
        assert app_log == "Swag Labs"

        prod.addproduct()
        prod.gotocart()


        cart = CartPage(driver)
        cart.checkout()

        checkout_info = CheckoutInformationPage(driver)
        checkout_info.enter_checkout_information("John", "Doe", "12345")

        checkout_overview = CheckoutOverviewPage(driver)
        checkout_overview.finish_checkout()

        assert "checkout-complete" in driver.current_url
    else:
        error_text = lgn.get_error_message()
        assert error_text == "Epic sadface: Username and password do not match any user in this service" or \
               error_text == "Epic sadface: Sorry, this user has been locked out." or \
               error_text == "Epic sadface: Username is required" or \
               error_text == "Epic sadface: Password is required"

    
