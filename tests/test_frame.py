from page_objects.FramePage import *


@allure.title('Check the text in iframe')
def test_iframe1(driver):
    frame = Frame(driver)
    frame.open_page()
    frame.switch_to_the_frame()
    frame.assert_that_text_in_frame_is_correct()
