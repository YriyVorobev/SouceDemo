import allure
import pytest
from allure_commons.types import Severity
from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class Checkout(BasePage):

    _PAGE_URL = Urls.CHECKOUT

    _CHECKOUT = "//button[@data-test='checkout']"

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    def click_button_checkout(self):
        with allure.step("Открытие страницы Checkout"):
            self.wait.until(EC.element_to_be_clickable(self._CHECKOUT)).click()

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="next checkout",
                attachment_type=allure.attachment_type.PNG
            )
            self.wait.until(EC.url_to_be(self._PAGE_URL))
