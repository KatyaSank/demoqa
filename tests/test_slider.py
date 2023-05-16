from page_objects.SliderPage import *


@allure.title('Check that slider is moved correct')
def test_slider(driver):
    slider = Slider(driver)
    slider.open_page()
    slider.move_slider()
    slider.assert_that_slider_moved_correct()
