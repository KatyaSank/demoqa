import allure

from page_objects.TextboxPage import TextBox


@allure.title('Check that input fields are visible')
def test_input_visible(driver):
    textbox = TextBox(driver)
    textbox.open_page()
    textbox.maximize_window()
    textbox.assert_that_full_name_is_displayed()
    textbox.assert_that_email_is_displayed()
    textbox.assert_that_current_address_is_displayed()
    textbox.assert_that_permanent_address_is_displayed()


@allure.title('Fill data into input fields and save it')
def test_text_box(driver):
    textbox = TextBox(driver)
    textbox.open_page()
    textbox.fill_field_full_name()
    textbox.fill_field_email()
    textbox.fill_field_current_address()
    textbox.fill_field_permanent_address()
    textbox.click_button()
    # driver.save_screenshot('test.png')
    textbox.assert_result_name()
    textbox.assert_result_email()
    textbox.assert_result_current_address()
    textbox.assert_result_permanent_address()
