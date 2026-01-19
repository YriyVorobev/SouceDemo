import allure
import pytest
from allure_commons.types import Severity
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from base.base_page import BasePage
from data.urls import Urls

class ProductsToCart(BasePage):

    _PAGE_URL = Urls.PRODUCTS_TO_CART

    _SELECTOR_TO_CART = "//select[@data-test='product-sort-container']"
    _BACK_SPACE = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    _LIGHT_BIKE = "//button[@data-test='add-to-cart-sauce-labs-bike-light']"
    _FLEECE_TSHIRT = "//button[@data-test='add-to-cart-sauce-labs-fleece-jacket']"
    _CART = "//a[@data-test='shopping-cart-link']"
    _CART_BADGE = "//span[@data-test='shopping-cart-badge']"

    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    def select_drop_down(self,select_value):
        with allure.step("Выбор из выпадающего списка"):
            select = self.wait.until(EC.presence_of_element_located(self._SELECTOR_TO_CART))
            Select(select).select_by_value(select_value)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Выбор из выпадающего списка",
                attachment_type=allure.attachment_type.PNG
            )
    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    def add_products(self):
        with allure.step("Добавления товаров в корзину"):
            self.wait.until(EC.element_to_be_clickable(self._BACK_SPACE)).click()
            self.wait.until(EC.element_to_be_clickable(self._LIGHT_BIKE)).click()
            self.wait.until(EC.element_to_be_clickable(self._FLEECE_TSHIRT)).click()

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Добавления товаров в корзину",
                attachment_type=allure.attachment_type.PNG
            )
    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    @allure.step("Ждем пока элемент корзина повиться и возвращаем число которое внутри корзины")
    def get_cart_badge_count(self)-> int:
        badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
        return int(badge.text)

    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    @allure.step("Проверка товаров в корзине")
    def assert_badge(self, expected: int):
        actual = self.get_cart_badge_count()
        assert actual == expected, f"Ожидали {expected} товаров в корзине, а отображается {actual}"

    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    def click_button_cart(self):
        with allure.step("Переход в корзину"):
            self.wait.until(EC.element_to_be_clickable(self._CART)).click()

            allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Добавления товаров в корзину",
            attachment_type=allure.attachment_type.PNG
            )

            self.wait.until(EC.url_contains(Urls.CART))
            assert Urls.CART in self.driver.current_url

