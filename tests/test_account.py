import faker

from base.base_test import BaseTest
from conftest import faker_ru
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

    @allure.story("next to checkout")
    def test_next_to_checkout(self):
        self.checkout.click_button_checkout()
        self.checkout.is_opened()

    @allure.story("information in checkout")
    def test_information_checkout(self,faker_ru):
        self.checkout_information.entering_a_name(faker_ru.first_name())
        self.checkout_information.entering_last_name(faker_ru.last_name())
        self.checkout_information.entering_zip_code(faker_ru.postcode())


