import allure
from page_objects.Base import Base


class Modal(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/modal-dialogs"
        self.small_modal_button = '//*[@id="showSmallModal"]'
        self.small_modal_text_locator = '//div[@class="modal-body"]'
        # / html / body / div[5] / div / div / div[2]
        self.small_modal_text = 'This is a small modal. It has very less content'
        self.small_modal_cross_button = '//span[@aria-hidden="true"]'
        self.small_modal_close_button = '//*[@id="closeSmallModal"]'
        self.empty_area = '//div[@role="dialog"]'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step('Open small modal window')
    def open_small_modal(self):
        return self.click(self.small_modal_button)

    @allure.step('Close small modal window with cross button')
    def close_small_modal_with_cross_button(self):
        return self.click(self.small_modal_cross_button)

    @allure.step('Close small modal window with close button')
    def close_small_modal_with_close_button(self):
        return self.click(self.small_modal_close_button)

    @allure.step('Close small modal window with empty area click')
    def close_small_modal_with_empty_area_click(self):
        return self.click(self.empty_area)

    @allure.step('Waiting for close modal')
    def waiting_until_close_button_visible(self):
        return self.wait_until_invisibility_of_element(self.small_modal_close_button)

    @allure.step('Check that text in small button is correct')
    def assert_that_text_in_small_modal_is_correct(self):
        assert self.get_element_text(self.small_modal_text_locator) == self.small_modal_text

    @allure.step('Check that small button is closed')
    def assert_that_small_modal_is_closed(self):
        assert not self.is_element_displayed(self.small_modal_close_button)

