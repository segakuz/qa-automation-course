from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, pytest

def answer():
    return math.log(int(time.time()))

pages = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('pages', pages)
class TestParametrize():
    def test_pages_answer(self, browser, pages):
        browser.get(pages)
        textarea = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.textarea'))
        )
        textarea.send_keys(str(answer()))
        button = browser.find_element_by_css_selector('.submit-submission')
        button.click()

        feedback_el = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))
        )

        feedback = feedback_el.text

        correct_feedback = 'Correct!'

        assert correct_feedback in feedback, print(feedback)
