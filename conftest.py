import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker


@pytest.fixture(autouse=True, scope="class")
def driver(request):

    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def faker_ru():
    faker = Faker("ru_RU")
    return faker