import allure
from page_objects.Base import Base


class Alert(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/alerts"
        self.simple_alert_button = '//*[@id="alertButton"]'
        self.delay_alert_button = '//*[@id="timerAlertButton"]'
        self.confirm_box_alert_button = '//*[@id="confirmButton"]'
        self.confirm_box_message = '//*[@id="confirmResult"]'
        self.prompt_box_alert_button = '//*[@id="promtButton"]'
        self.accept_message = 'You selected Ok'
        self.decline_message = 'You selected Cancel'
        self.text_to_prompt_alert = 'Katya'
        self.prompt_box_message = '//*[@id="promptResult"]'
        self.prompt_message = f'You entered {self.text_to_prompt_alert}'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def open_simple_alert(self):
        return self.click(self.simple_alert_button)

    @allure.step
    def assert_that_alert_is_closed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.simple_alert_button)

    @allure.step
    def open_delay_alert(self):
        return self.click(self.delay_alert_button)

    @allure.step
    def assert_that_delay_alert_is_closed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.delay_alert_button)

    @allure.step
    def open_confirm_box_alert(self):
        return self.click(self.confirm_box_alert_button)

    @allure.step
    def assert_that_accept_message_for_confirm_box_alert_is_correct(self):
        assert self.get_element_text(self.confirm_box_message) == self.accept_message

    @allure.step
    def assert_that_decline_message_for_confirm_box_alert_is_correct(self):
        assert self.get_element_text(self.confirm_box_message) == self.decline_message

    @allure.step
    def open_prompt_box_alert(self):
        return self.click(self.prompt_box_alert_button)

    @allure.step
    def switch_to_alert_and_fill_text_to_field(self):
        return self.switch_to_alert_and_fill_text(self.text_to_prompt_alert)

    @allure.step
    def assert_that_prompt_message_for_prompt_box_alert_is_correct(self):
        assert self.get_element_text(self.prompt_box_message) == self.prompt_message

    @allure.step
    def assert_that_prompt_message_for_prompt_box_alert_is_not_displayed(self):
        assert not self.is_element_displayed(self.prompt_box_message)
