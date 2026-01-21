import allure
import pytest
from allure_commons.types import Severity
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from data.urls import Urls

class CheckoutInformation(BasePage):

    _PAGE_URL = Urls.CHECKOUT
    _FIRST_NAME = "//input[@data-test='firstName']"
    _LAST_NAME = "//input[@data-test='lastName']"
    _ZIP_CODE = "//input[@data-test='postalCode']"

    @pytest.mark.regression
    @allure.severity(Severity.BLOCKER)
    def entering_a_name(self,firstname):
        with allure.step(f"Очистить поле ввода {firstname} и ввести новое значение"):
            first_name = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME))
            first_name.send_keys(Keys.CONTROL + "a")
            first_name.send_keys(Keys.BACKSPACE)
            current_first_name = first_name.get_attribute("value")
            first_name.send_keys(firstname)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Имя пользователя введено",
                attachment_type=allure.attachment_type.PNG
            )
            assert current_first_name != first_name, f"Поле {first_name} не заполненно"
