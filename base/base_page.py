from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_lockator import MetaLocator
import allure

class BasePage(metaclass=MetaLocator):

    def __init__(self,driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver,timeout=10,poll_frequency=10)
        self.action = ActionChains(self.driver)

    def open(self):
        with allure.step(f"Open {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)

    def is_opened(self):
        with allure.step(f"Opened {self._PAGE_URL}"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
