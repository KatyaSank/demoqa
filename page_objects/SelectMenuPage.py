import allure
from page_objects.Base import Base


class Select(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/select-menu"
        self.old_style_dropdown = '//*[@id="oldSelectMenu"]'
        self.old_style_value_white = '7'
        self.white_option = '//*[@id="oldSelectMenu"]/option[8]'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step('Select value from dropdown')
    def select_value_from_dropdown(self):
        return self.select_by_id_value(self.old_style_dropdown, self.old_style_value_white)

    @allure.step('Check that correct value selected from dropdown')
    def assert_selected_value_from_dropdown(self):
        return self.assert_that_element_is_selected_by_xpath(self.white_option)
