from selenium import webdriver
import time, os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_el = browser.find_element_by_css_selector("input[name='firstname']")
    first_name_el.send_keys("Name")

    last_name_el = browser.find_element_by_css_selector("input[name='lastname']")
    last_name_el.send_keys("Surname")

    email_el = browser.find_element_by_css_selector("input[name='email']")
    email_el.send_keys("Email")

    element = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '_example.txt')
    element.send_keys(file_path)

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
