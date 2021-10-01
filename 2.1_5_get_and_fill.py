from selenium import webdriver
import math, time

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()



finally:
    time.sleep(5)
    browser.quit()
