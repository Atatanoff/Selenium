from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_basket_button_exists(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(5)
    btn = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert btn, 'button not found'

    