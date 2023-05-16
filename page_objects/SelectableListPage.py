import allure
from page_objects.Base import Base


class SelectableList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/selectable"
        self.first_line_locator = '//*[@id="verticalListContainer"]/li[1]'
        self.second_line_locator = '//*[@id="verticalListContainer"]/li[2]'
        self.third_line_locator = '//*[@id="verticalListContainer"]/li[3]'
        self.fourth_line_locator = '//*[@id="verticalListContainer"]/li[4]'
        self.selected_line = 'mt-2 list-group-item active list-group-item-action'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def assert_that_first_line_is_selected(self):
        assert self.get_attribute_by_class(self.first_line_locator) == self.selected_line

    @allure.step
    def assert_that_second_line_is_selected(self):
        assert self.get_attribute_by_class(self.second_line_locator) == self.selected_line

    @allure.step
    def assert_that_third_line_is_selected(self):
        assert self.get_attribute_by_class(self.third_line_locator) == self.selected_line

    @allure.step
    def assert_that_fourth_line_is_selected(self):
        assert self.get_attribute_by_class(self.fourth_line_locator) == self.selected_line

    @allure.step
    def assert_that_first_line_is_not_selected(self):
        assert not self.get_attribute_by_class(self.first_line_locator) == self.selected_line

    @allure.step
    def assert_that_second_line_is_not_selected(self):
        assert not self.get_attribute_by_class(self.second_line_locator) == self.selected_line

    @allure.step
    def assert_that_third_line_is_not_selected(self):
        assert not self.get_attribute_by_class(self.third_line_locator) == self.selected_line

    @allure.step
    def assert_that_fourth_line_is_not_selected(self):
        assert not self.get_attribute_by_class(self.fourth_line_locator) == self.selected_line

    @allure.step
    def click_first_line(self):
        return self.click(self.first_line_locator)

    @allure.step
    def click_second_line(self):
        return self.click(self.second_line_locator)

    @allure.step
    def click_third_line(self):
        return self.click(self.third_line_locator)

    @allure.step
    def click_fourth_line(self):
        return self.click(self.fourth_line_locator)
