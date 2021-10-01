from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element_by_css_selector('#book')
    button.click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    button2 = browser.find_element_by_css_selector('form button[type="submit"]')
    button2.click()   

    time.sleep(10)

finally:
    browser.quit()
