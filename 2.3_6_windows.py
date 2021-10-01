from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.trollface[type="submit"]')
    button.click()

    cur_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    button2 = browser.find_element_by_css_selector('form button[type="submit"]')
    button2.click()   

finally:
    time.sleep(10)
    browser.quit()
