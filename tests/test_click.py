from page_objects.ClickPage import *


@allure.title('Click using double click')
def test_double_click(driver):
    click = Click(driver)
    click.open_page()
    click.use_double_click()
    click.assert_that_double_click_result_message_is_displayed()


@allure.title('Click using right click')
def test_right_click(driver):
    click = Click(driver)
    click.open_page()
    click.use_right_click()
    click.assert_that_right_click_result_message_is_displayed()
