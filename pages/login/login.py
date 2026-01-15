import allure
from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    _PAGE_URL = Urls.LOGIN_PAGE
    _USER_NAME_FIELD = "//input[@data-test='username']"
    _PASSWORD_FIELD = "//input[@data-test='password']"
    _SUBMIT_BUTTON = "//input[@data-test='login-button']"

    def login(self,username, password):
        with allure.step(f"Вход в систему через {username} и {password}"):
            self.wait.until(EC.visibility_of_element_located(self._USER_NAME_FIELD)).send_keys(username)
            self.wait.until(EC.visibility_of_element_located(self._PASSWORD_FIELD)).send_keys(password)
            self.wait.until(EC.visibility_of_element_located(self._SUBMIT_BUTTON)).click()

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Вход в систему",
                attachment_type= allure.attachment_type.PNG
            )

