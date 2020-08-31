import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_backet_button_check(browser):
    browser.get(link)
    #time.sleep(30)
    try:
        browser.find_element_by_class_name("btn-add-to-basket")
    except NoSuchElementException:
        assert False, "ADD-TO-BASKET BUTTON IS NOT PRESENT!"
