import time
from page_objects.AccordianPage import *


@allure.title('Test expand and collapse modes for accordian')
def test_accordian(driver):
    accordian = Accordian(driver)
    accordian.open_page()
    accordian.assert_that_first_box_is_expand()
    accordian.click_first_box()
    time.sleep(1)
    accordian.assert_that_first_box_is_collapsed()
    accordian.assert_that_third_box_is_collapsed()
    accordian.assert_that_third_box_is_collapsed()
    accordian.click_second_box()
    time.sleep(1)
    accordian.assert_that_second_box_is_expand()
    accordian.scroll_to_bottom()
    accordian.click_third_box()
    time.sleep(1)
    accordian.assert_that_third_box_is_expand()
