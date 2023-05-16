from page_objects.NestedFramePage import *


@allure.title('Check the text into the child iframe')
def test_iframe1(driver):
    nested = NestedFrame(driver)
    nested.open_page()
    nested.switch_to_the_parent_frame()
    nested.assert_that_text_in_parent_frame_is_correct()
    nested.switch_to_the_child_frame()
    nested.assert_that_text_in_child_frame_is_correct()

