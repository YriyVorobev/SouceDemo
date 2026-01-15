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