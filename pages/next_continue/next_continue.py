import pytest
import allure
from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity


class NextContinue(BasePage):

    _PAGE_URL = Urls.CONTINUE
    _SUBMIT_BUTTON_CONTINUE = "//input[@data-test='continue']"

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    def submit_button_continue(self):
        with allure.step("Нажатие по кнопе продолжить"):
            self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON_CONTINUE)).click()


