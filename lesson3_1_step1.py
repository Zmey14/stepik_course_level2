from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://stepik.org/lesson/187065/step/11?unit=161976"

try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    browser.quit()