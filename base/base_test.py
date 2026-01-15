from data.credentials import Credentials
from pages.login.login import LoginPage


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
