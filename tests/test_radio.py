from page_objects.RadioPage import *


@allure.title('Check that only one radio button can be selected')
def test_radio(driver):
    radio = Radio(driver)
    radio.open_page()
    radio.click_impressive()
    radio.assert_that_impressive_is_displayed()
    radio.assert_that_yes_is_not_displayed()
    radio.click_yes()
    radio.assert_that_yes_is_displayed()
    radio.assert_that_impressive_is_not_displayed()
