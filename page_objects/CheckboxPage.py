import allure
from page_objects.Base import Base


class Checkbox(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/checkbox'
        self.plus_button = '//*[@id="tree-node"]/div/button[1]'
        self.checkbox_office = '//span[text()="Office"]'
        self.result_office = '//span[text()="office"]'
        self.result_public = '//span[text()="public"]'
        self.result_private = '//span[text()="private"]'
        self.result_classfield = '//span[text()="classified"]'
        self.result_general = '//span[text()="general"]'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step('Expand checkboxes tree')
    def expand_tree(self):
        return self.click(self.plus_button)

    @allure.step('Click "office" checkbox')
    def click_checkbox_office(self):
        return self.click(self.checkbox_office)

    @allure.step('Check that result message consist of "office"')
    def assert_that_office_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_office)

    @allure.step('Check that result message consist of "public"')
    def assert_that_public_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_public)

    @allure.step('Check that result message consist of "private"')
    def assert_that_private_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_private)

    @allure.step('Check that result message consist of "classfield"')
    def assert_that_classfield_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_classfield)

    @allure.step('Check that result message consist of "general"')
    def assert_that_general_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_general)
