from page_objects.TipsPage import *


@allure.title('Check that tips for different elements is displayed correct')
def test_tool_tips(driver):
    tips = Tips(driver)
    tips.open_page()
    tips.maximize_window()
    tips.hover_the_button()
    tips.assert_that_button_tips_is_correct()
    tips.hover_the_text_field()
    tips.assert_that_text_field_tips_is_correct()
    tips.hover_the_contrary_container()
    tips.assert_that_contrary_container_tips_is_correct()
    tips.hover_the_section_container()
    tips.assert_that_section_container_tips_is_correct()
