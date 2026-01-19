import pytest
import allure
from allure_commons.types import Severity
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from data.urls import Urls

class DeleteCartProduct(BasePage):

    _PAGE_URL = Urls.CART
    _REMOVE_BACK_SPACE = "//button[@data-test='remove-sauce-labs-backpack']"

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    def delete_cart_product(self):
        with allure.step("Удаление продукта из корзины и проверка что продукт удалился"):
            self.wait.until(EC.element_to_be_clickable(self._REMOVE_BACK_SPACE)).click()

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="delete products cart",
                attachment_type=allure.attachment_type.PNG
            )

            self.wait.until(EC.invisibility_of_element(self._REMOVE_BACK_SPACE))
