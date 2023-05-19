import allure
from page_objects.Base import Base


class Accordian(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/accordian"
        self.first_box_locator = '//*[@id="accordianContainer"]/div/div[1]/div[2]'
        self.second_box_locator = '//*[@id="accordianContainer"]/div/div[1]/div[2]'
        self.third_box_locator = '//*[@id="accordianContainer"]/div/div[2]/div[2]'
        self.box_status_expand = 'collapse show'
        self.box_status_collapse = 'collapse'
        self.first_box = '//*[@id="section1Heading"]'
        self.second_box = '//*[@id="section1Heading"]'
        self.third_box = '//*[@id="section2Heading"]'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step('Click on the first line')
    def click_first_box(self):
        return self.click(self.first_box)

    @allure.step('Click on the second line')
    def click_second_box(self):
        return self.click(self.second_box)

    @allure.step('Click on the third line')
    def click_third_box(self):
        return self.click(self.third_box)

    @allure.step('Check, that first line is expended')
    def assert_that_first_box_is_expand(self):
        assert self.get_attribute_by_class(self.first_box_locator) == self.box_status_expand

    @allure.step('Check, that first line is collapsed')
    def assert_that_first_box_is_collapsed(self):
        assert self.get_attribute_by_class(self.first_box_locator) == self.box_status_collapse

    @allure.step('Check, that second line is expanded')
    def assert_that_second_box_is_expand(self):
        assert self.get_attribute_by_class(self.second_box_locator) == self.box_status_expand

    @allure.step('Check, that second line is collapsed')
    def assert_that_second_box_is_collapsed(self):
        assert self.get_attribute_by_class(self.second_box_locator) == self.box_status_collapse

    @allure.step('Check, that third line is expanded')
    def assert_that_third_box_is_expand(self):
        assert self.get_attribute_by_class(self.third_box_locator) == self.box_status_expand

    @allure.step('Check, that third line is collapsed')
    def assert_that_third_box_is_collapsed(self):
        assert self.get_attribute_by_class(self.third_box_locator) == self.box_status_collapse
