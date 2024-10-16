import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_guest_should_see_button_adding_items_in_card(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    try:
        button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except NoSuchElementException:
        button = None

    assert button is not None, "Кнопка добавления товара в корзину не найдена"

    time.sleep(2)
