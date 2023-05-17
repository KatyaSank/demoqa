from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        return self.driver.get(url)

    def maximize_window(self):
        return self.driver.maximize_window()

    def get_locator_by_xpath(self, selector):
        xpath = (By.XPATH, selector)
        return self.driver.find_element(*xpath)

    def click(self, selector):
        element = self.get_locator_by_xpath(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def double_click(self, selector):
        ActionChains(self.driver).double_click(self.get_locator_by_xpath(selector)).perform()

    def right_click(self, selector):
        ActionChains(self.driver).context_click(self.get_locator_by_xpath(selector)).perform()

    def hover(self, selector):
        ActionChains(self.driver).click(self.get_locator_by_xpath(selector)).perform()

    def move_element(self, selector, coord_x, coord_y):
        ActionChains(self.driver).click_and_hold(self.get_locator_by_xpath(selector)).move_by_offset(coord_x, coord_y).\
            release().perform()

    def fill_field(self, selector, text):
        element = self.get_locator_by_xpath(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(text)

    def clear(self, selector):
        return self.get_locator_by_xpath(selector).clear()

    def scroll_to_bottom(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_element_text(self, selector):
        return self.get_locator_by_xpath(selector).text

    def select_by_id_value(self, selector, value):
        return Select(self.get_locator_by_xpath(selector)).select_by_value(*value)

    def get_attribute_by_xpath_any_attribute(self, selector, name):
        return self.get_locator_by_xpath(selector).get_attribute(name)

    def get_attribute_by_class(self, selector):
        return self.get_locator_by_xpath(selector).get_attribute('class')

    def get_attribute_by_value(self, selector):
        return self.get_locator_by_xpath(selector).get_attribute('value')

    def assert_that_element_is_displayed_by_xpath(self, selector):
        assert self.get_locator_by_xpath(selector).is_displayed()

    def assert_that_element_is_selected_by_xpath(self, selector):
        return self.get_locator_by_xpath(selector).is_selected()

    def get_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    def switch_to_alert_and_fill_text(self, name):
        alert = self.driver.switch_to.alert
        alert.send_keys(name)
        alert.accept()

    def switch_to_alert_and_accept_it(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def switch_to_alert_and_decline_it(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def switch_to_frame(self, selector):
        return self.driver.switch_to.frame(self.get_locator_by_xpath(selector))

    def is_element_displayed(self, selector):
        try:
            if self.get_locator_by_xpath(selector):
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def scroll_to_top(self):
        return self.driver.execute_script("scroll(0, 0);")




