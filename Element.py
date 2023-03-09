from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    y_element.send_keys(y)

    r_el = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    r_el.click()

    r = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", r)
    r.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:

    time.sleep(10)

    browser.quit()
