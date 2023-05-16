import allure
from page_objects.Base import Base


class Click(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/buttons"
        self.double_click_button = '//*[@id="doubleClickBtn"]'
        self.result_double_click = '//*[@id="doubleClickMessage"]'
        self.double_click_result_message = 'You have done a double click'
        self.right_click_button = '//*[@id="rightClickBtn"]'
        self.result_right_click = '//*[@id="rightClickMessage"]'
        self.right_click_result_message = 'You have done a right click'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def use_double_click(self):
        return self.double_click(self.double_click_button)

    @allure.step
    def assert_that_double_click_result_message_is_displayed(self):
        assert self.get_element_text(self.result_double_click) == self.double_click_result_message

    @allure.step
    def use_right_click(self):
        return self.right_click(self.right_click_button)

    @allure.step
    def assert_that_right_click_result_message_is_displayed(self):
        assert self.get_element_text(self.result_right_click) == self.right_click_result_message



