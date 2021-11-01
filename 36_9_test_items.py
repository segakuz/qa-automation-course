import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket')

    assert len(button) > 0, "'Add to cart' button is not present"
