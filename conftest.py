import pytest

from selenium import webdriver



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")

def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name =="chrome":
        driver = webdriver.Chrome(executable_path="C:\\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.rahulshettyacademy.com/angularpractice")
        driver.maximize_window()
    #elif browser_name=="firefox":
        #firefox path invocation
    #elif browser_name=="IE":
        #IE path invocation
    request.cls.driver = driver
    yield
    driver.close()

