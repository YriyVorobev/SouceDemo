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
    def entering_a_name(self,firstname: str):
        with allure.step(f"Очистить поле ввода {firstname} и ввести новое значение"):
            first_name = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME))

            first_name.send_keys(Keys.CONTROL + "a")
            first_name.send_keys(Keys.BACKSPACE)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="first_name знчение очищенно",
                attachment_type=allure.attachment_type.PNG
            )

            current_first_name = first_name.get_attribute("value")
            first_name.send_keys(firstname)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="first_name значение заполнено",
                attachment_type=allure.attachment_type.PNG
            )
            assert current_first_name != first_name, f"Поле {firstname} не заполнено"

    @pytest.mark.regression
    @allure.severity(Severity.BLOCKER)
    def entering_last_name(self,lastname: str):
        with allure.step(f"Заполняем {lastname} значние"):
            last_name = self.wait.until(EC.element_to_be_clickable(self._LAST_NAME))

            last_name.send_keys(Keys.CONTROL + "a")
            last_name.send_keys(Keys.BACKSPACE)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="last_name значение очищенно",
                attachment_type=allure.attachment_type.PNG
            )

            current_last_name = last_name.get_attribute("value")

            last_name.send_keys(lastname)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="last_name занчение заполнено",
                attachment_type=allure.attachment_type.PNG
            )

            assert current_last_name != last_name, f"Поле {lastname}  не заполнено"

    def entering_zip_code(self,postalcode :str):
        with allure.step(f"Заполняем {postalcode} значения"):
            postal_code = self.wait.until(EC.element_to_be_clickable(self._ZIP_CODE))

            postal_code.send_keys(Keys.CONTROL + "a")
            postal_code.send_keys(Keys.BACKSPACE)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Очищаем поле postal_code",
                attachment_type=allure.attachment_type.PNG
            )

            current_postal_code = postal_code.get_attribute("value")
            postal_code.send_keys(postalcode)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Заполняем поле postal_code",
                attachment_type=allure.attachment_type.PNG
            )

            assert current_postal_code != postal_code, f"Поле {postalcode} не заполнено"
