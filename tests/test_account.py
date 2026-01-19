from base.base_test import BaseTest
from data.credentials import Credentials
import allure


@allure.epic("Test_changed")
@allure.feature("Test login")
class TestAccount(BaseTest):

    @allure.story("Test login")
    def test_login(self):
        self.login_page.open()
        self.login_page.login(
            username=Credentials.LOGIN,
            password=Credentials.PASSWORD
        )
    @allure.story("Test adding to cart")
    def test_to_cart(self):
        self.products_page.is_opened()
        self.products_page.select_drop_down("lohi")
        self.products_page.add_products()
        self.products_page.assert_badge(3)
        self.products_page.click_button_cart()

    @allure.story("Test delete products cart")
    def test_delete_cart(self):
        self.delete_cart_products.is_opened()
        self.delete_cart_products.delete_cart_product()
