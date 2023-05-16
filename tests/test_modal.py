import time
from page_objects.ModalPage import *


@allure.title('Check closing modal with cross button')
def test_close_modal_with_cross_button(driver):
    modal = Modal(driver)
    modal.open_page()
    modal.open_small_modal()
    modal.assert_that_text_in_small_modal_is_correct()
    modal.close_small_modal_with_cross_button()
    time.sleep(2)
    modal.assert_that_small_modal_is_closed()


@allure.title('Check closing modal with close button')
def test_close_modal_with_close_button(driver):
    modal = Modal(driver)
    modal.open_page()
    modal.open_small_modal()
    modal.assert_that_text_in_small_modal_is_correct()
    modal.close_small_modal_with_close_button()
    time.sleep(2)
    modal.assert_that_small_modal_is_closed()


@allure.title('Check closing modal with free button')
def test_close_modal_with_free_area(driver):
    modal = Modal(driver)
    modal.open_page()
    modal.open_small_modal()
    modal.assert_that_text_in_small_modal_is_correct()
    modal.close_small_modal_with_empty_area_click()
    time.sleep(2)
    modal.assert_that_small_modal_is_closed()
