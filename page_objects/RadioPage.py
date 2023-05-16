import allure
from page_objects.Base import Base


class Radio(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/radio-button"
        self.impressive = '//label[@for="impressiveRadio"]'
        self.yes = '//label[@for="yesRadio"]'
        self.result_impressive = '//span[text()="Impressive"]'
        self.result_yes = '//span[text()="Yes"]'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def click_impressive(self):
        return self.click(self.impressive)

    @allure.step
    def assert_that_impressive_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_impressive)

    @allure.step
    def assert_that_impressive_is_not_displayed(self):
        assert not self.is_element_displayed(self.result_impressive)

    @allure.step
    def click_yes(self):
        return self.click(self.yes)

    @allure.step
    def assert_that_yes_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_yes)

    @allure.step
    def assert_that_yes_is_not_displayed(self):
        assert not self.is_element_displayed(self.result_yes)


