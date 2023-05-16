import allure
from page_objects.Base import Base


class Frame(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/frames"
        self.frame = '//*[@id="frame1"]'
        self.frame_title = '//*[@id="sampleHeading"]'
        self.frame_title_text = 'This is a sample page'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def switch_to_the_frame(self):
        return self.switch_to_frame(self.frame)

    @allure.step
    def assert_that_text_in_frame_is_correct(self):
        assert self.get_element_text(self.frame_title) == self.frame_title_text
