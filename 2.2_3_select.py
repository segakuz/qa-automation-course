from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time

link = "http://suninjuly.github.io/selects1.html"

def calc(x, y):
    return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text

    sum = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()



finally:
    time.sleep(5)
    browser.quit()
