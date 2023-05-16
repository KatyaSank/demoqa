import allure
from page_objects.Base import Base


class TextBox(Base):
    NAME = "Katya"
    EMAIL = "Kate@gmail.com"
    CURRENT_ADDRESS = "Klaipeda"
    PERMANENT_ADDRESS = "World"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/text-box'
        self.full_name = '//*[@id="userName"]'
        self.email = '//*[@id="userEmail"]'
        self.current_address = '//*[@id="currentAddress"]'
        self.permanent_address = '//*[@id="permanentAddress"]'
        self.submit = '//*[@id="submit"]'
        self.result_name = '//*[@id="name"]'
        self.result_email = '//*[@id="email"]'
        self.result_current_address = '//*[@id="currentAddress"]'
        self.result_permanent_address = '//*[@id="permanentAddress"]'

    @allure.step
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def assert_that_full_name_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.full_name)

    @allure.step
    def assert_that_email_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.email)

    @allure.step
    def assert_that_current_address_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.current_address)

    @allure.step
    def assert_that_permanent_address_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.permanent_address)

    @allure.step
    def fill_field_full_name(self):
        return self.fill_field(self.full_name, self.NAME)

    @allure.step
    def fill_field_email(self):
        return self.fill_field(self.email, self.EMAIL)

    @allure.step
    def fill_field_current_address(self):
        return self.fill_field(self.current_address, self.CURRENT_ADDRESS)

    @allure.step
    def fill_field_permanent_address(self):
        return self.fill_field(self.permanent_address, self.PERMANENT_ADDRESS)

    @allure.step
    def click_button(self):
        self.scroll_to_bottom()
        return self.click(self.submit)

    @allure.step
    def assert_result_name(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_name)

    @allure.step
    def assert_result_email(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_email)

    @allure.step
    def assert_result_current_address(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_current_address)

    @allure.step
    def assert_result_permanent_address(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_permanent_address)




