from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_basket_button_present(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    WebDriverWait(browser, 6).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, "img")))
    buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(buttons) == 1