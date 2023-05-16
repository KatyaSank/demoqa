import allure
from page_objects.Base import Base


class Tips(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/tool-tips"
        self.button_locator = '//*[@id="toolTipButton"]'
        self.attribute = 'aria-describedby'
        self.button_tips = 'buttonToolTip'
        self.text_field_locator = '//*[@id="toolTipTextField"]'
        self.text_field_tips = 'textFieldToolTip'
        self.contrary_locator = '//*[@id="texToolTopContainer"]/a[1]'
        self.contrary_tips = 'contraryTexToolTip'
        self.section_locator = '//*[@id="texToolTopContainer"]/a[2]'
        self.section_tips = 'sectionToolTip'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def hover_the_button(self):
        return self.hover(self.button_locator)

    @allure.step
    def assert_that_button_tips_is_correct(self):
        assert self.get_attribute_by_xpath_any_attribute(self.button_locator, self.attribute) == self.button_tips

    @allure.step
    def hover_the_text_field(self):
        return self.hover(self.text_field_locator)

    @allure.step
    def assert_that_text_field_tips_is_correct(self):
        assert self.get_attribute_by_xpath_any_attribute(self.text_field_locator, self.attribute) == self.text_field_tips

    @allure.step
    def hover_the_contrary_container(self):
        return self.hover(self.contrary_locator)

    @allure.step
    def assert_that_contrary_container_tips_is_correct(self):
        assert self.get_attribute_by_xpath_any_attribute(self.contrary_locator, self.attribute) == self.contrary_tips

    @allure.step
    def hover_the_section_container(self):
        return self.hover(self.section_locator)

    @allure.step
    def assert_that_section_container_tips_is_correct(self):
        assert self.get_attribute_by_xpath_any_attribute(self.section_locator, self.attribute) == self.section_tips



