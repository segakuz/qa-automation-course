from selenium import webdriver
import time, unittest

class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name_el = browser.find_element_by_css_selector(".first_block .first")
        first_name_el.send_keys("Name")

        last_name_el = browser.find_element_by_css_selector(".first_block .second")
        last_name_el.send_keys("Surname")

        email_el = browser.find_element_by_css_selector(".first_block .third")
        email_el.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        greeting = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        self.assertEqual(welcome_text, greeting, f"Expected, that {welcome_text} should be equal {greeting}")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_el = browser.find_element_by_css_selector(".first_block .first")
        first_name_el.send_keys("Name")

        last_name_el = browser.find_element_by_css_selector(".first_block .second")
        last_name_el.send_keys("Surname")

        email_el = browser.find_element_by_css_selector(".first_block .third")
        email_el.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        greeting = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, greeting, f"Expected, that {welcome_text} should be equal {greeting}")


if __name__ == '__main__':
    unittest.main()
