from page_objects.AlertsPage import *


@allure.title('Open simple alert and close it by "OK" button')
def test_alert(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_simple_alert()
    alert.switch_to_alert_and_accept_it()
    alert.assert_that_alert_is_closed()


@allure.title('Open simple alert, waiting it loading and close it by "OK" button')
def test_delay_alert(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_delay_alert()
    alert.get_alert()
    alert.switch_to_alert_and_accept_it()
    alert.assert_that_delay_alert_is_closed()


@allure.title('Open confirmation alert and close it by "OK" button')
def test_confirmation_alert_accept(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_confirm_box_alert()
    alert.switch_to_alert_and_accept_it()
    alert.assert_that_accept_message_for_confirm_box_alert_is_correct()


@allure.title('Open confirmation alert and close it by "Cancel" button')
def test_confirmation_alert_dismiss(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_confirm_box_alert()
    alert.switch_to_alert_and_decline_it()
    alert.assert_that_decline_message_for_confirm_box_alert_is_correct()


@allure.title('Open prompt alert, fill the text and close it by "OK" button')
def test_prompt_alert(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_prompt_box_alert()
    alert.switch_to_alert_and_fill_text_to_field()
    alert.assert_that_prompt_message_for_prompt_box_alert_is_correct()


@allure.title('Open prompt alert and close it by "Cancel" button without filled text')
def test_prompt_alert_decline(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_prompt_box_alert()
    alert.switch_to_alert_and_decline_it()
    alert.assert_that_prompt_message_for_prompt_box_alert_is_not_displayed()


@allure.title('Open prompt alert and close it by "OK" button without filled text')
def test_prompt_alert_accept(driver):
    alert = Alert(driver)
    alert.open_page()
    alert.open_prompt_box_alert()
    alert.switch_to_alert_and_accept_it()
    alert.assert_that_prompt_message_for_prompt_box_alert_is_not_displayed()
