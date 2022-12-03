import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None
@pytest.fixture
def setup():
    print("start browser")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")

def test_1(setup):
    driver.get("https://facebook.com")
    print("test1 ran")

def test_2(setup):
    driver.get("https://google.com")
    print("test2 ran")

def test_3(setup):
    driver.get("https://gmail.com")
    print("test3 ran")
