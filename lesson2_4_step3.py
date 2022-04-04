from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    number_x = browser.find_element(By.ID, "input_value").text
    result = calc(number_x)

    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(result)

    button_2 = browser.find_element(By.ID, "solve")
    button_2.click()

    copy_text = browser.switch_to.alert.text
    addToCopy = copy_text.split(":")[-1]
    pyperclip.copy(addToCopy)

finally:
    browser.quit()