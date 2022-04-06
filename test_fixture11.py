import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.ID, "login_link")


languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    ("ua", "украинский"),
    ("en-gb", "английский")
]

@pytest.mark.parametrize("code, lang", languages)
def test_guest_should_see_login_link(browser, code, lang):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    browser.get(link)
    print("Проверяемый язык %s" % lang)