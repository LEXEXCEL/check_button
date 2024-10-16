from selenium.webdriver.common.by import By


def test_guest_should_see_button_adding_items_in_card(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
