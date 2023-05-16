from page_objects.CheckboxPage import *


@allure.title('Test check/uncheck boxes')
def test_checkbox(driver):
    checkbox = Checkbox(driver)
    checkbox.open_page()
    checkbox.expand_tree()
    checkbox.click_checkbox_office()
    checkbox.assert_that_office_is_displayed()
    checkbox.assert_that_public_is_displayed()
    checkbox.assert_that_private_is_displayed()
    checkbox.assert_that_classfield_is_displayed()
    checkbox.assert_that_general_is_displayed()

