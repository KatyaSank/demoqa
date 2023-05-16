import allure
from page_objects.Base import Base


class Slider(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/slider"
        self.slider_locator = '//*[@id="sliderContainer"]/div[1]/span/input'
        self.coordinate_x = 100
        self.coordinate_y = 0
        self.slider_result_value = '81'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def move_slider(self):
        return self.move_element(self.slider_locator, self.coordinate_x, self.coordinate_y)

    @allure.step
    def assert_that_slider_moved_correct(self):
        assert self.get_attribute_by_value(self.slider_locator) == self.slider_result_value


