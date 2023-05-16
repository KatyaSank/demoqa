import allure
from page_objects.Base import Base


class NestedFrame(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/nestedframes"
        self.frame = '//*[@id="frame1"]'
        self.nested_frame = '/html/body/iframe'
        self.parent_frame_text = 'Parent frame'
        self.child_frame_text = 'Child Iframe'
        self.frame_text_locator = '/html/body'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def switch_to_the_parent_frame(self):
        return self.switch_to_frame(self.frame)

    @allure.step
    def switch_to_the_child_frame(self):
        return self.switch_to_frame(self.nested_frame)

    @allure.step
    def assert_that_text_in_parent_frame_is_correct(self):
        assert self.get_element_text(self.frame_text_locator) == self.parent_frame_text

    @allure.step
    def assert_that_text_in_child_frame_is_correct(self):
        assert self.get_element_text(self.frame_text_locator) == self.child_frame_text
