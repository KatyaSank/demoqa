import allure
from page_objects.Base import Base


class Table(Base):
    NAME = "Katie"
    SURNAME = "Sankovich"
    EMAIL = "Katya@gmail.com"
    AGE = '99'
    SALARY = '999'
    DEPARTMENT = "QA"
    NEW_NAME = 'Katerina'
    NEW_AGE = '1'

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/webtables"
        self.add_button = '//*[@id="addNewRecordButton"]'
        self.first_name = '//*[@id="firstName"]'
        self.last_name = '//*[@id="lastName"]'
        self.email = '//*[@id="userEmail"]'
        self.age = '//*[@id="age"]'
        self.salary = '//*[@id="salary"]'
        self.department = '//*[@id="department"]'
        self.submit_button = '//*[@id="submit"]'
        self.result_email = '//div[text()="Katya@gmail.com"]'
        self.result_first_name = f'//div[text()="{self.NEW_NAME}"]'
        self.result_age = f'//div[text()="{self.NEW_AGE}"]'
        self.registration_form_modal = '//*[@class="modal-header"]'
        self.edit_button = '//*[@id="edit-record-4"]'

    @allure.step('Open page')
    def open_page(self):
        return self.get_url(self.url)

    @allure.step
    def open_registration_form(self):
        return self.click(self.add_button)

    @allure.step
    def fill_first_name_field(self):
        return self.fill_field(self.first_name, self.NAME)

    @allure.step
    def fill_last_name_field(self):
        return self.fill_field(self.last_name, self.SURNAME)

    @allure.step
    def fill_email_field(self):
        return self.fill_field(self.email, self.EMAIL)

    @allure.step
    def fill_age_field(self):
        return self.fill_field(self.age, self.AGE)

    @allure.step
    def fill_salary_field(self):
        return self.fill_field(self.salary, self.SALARY)

    @allure.step
    def fill_department_field(self):
        return self.fill_field(self.department, self.DEPARTMENT)

    @allure.step
    def click_submit_button(self):
        return self.click(self.submit_button)

    @allure.step
    def assert_that_first_name_is_filled_correct(self):
        assert self.get_attribute_by_value(self.first_name) == self.NAME

    @allure.step
    def assert_that_last_name_is_filled_correct(self):
        assert self.get_attribute_by_value(self.last_name) == self.SURNAME

    @allure.step
    def assert_that_email_is_filled_correct(self):
        assert self.get_attribute_by_value(self.email) == self.EMAIL

    @allure.step
    def assert_that_age_is_filled_correct(self):
        assert self.get_attribute_by_value(self.age) == self.AGE

    @allure.step
    def assert_that_salary_is_filled_correct(self):
        assert self.get_attribute_by_value(self.salary) == self.SALARY

    @allure.step
    def assert_that_department_is_filled_correct(self):
        assert self.get_attribute_by_value(self.department) == self.DEPARTMENT

    @allure.step
    def assert_that_email_is_displayed_on_table(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_email)

    @allure.step
    def assert_that_modal_is_displayed(self):
        return self.assert_that_element_is_displayed_by_xpath(self.registration_form_modal)

    @allure.step
    def open_edit_mode(self):
        return self.click(self.edit_button)

    @allure.step
    def clear_age_field(self):
        return self.clear(self.age)

    @allure.step
    def clear_first_name_field(self):
        return self.clear(self.first_name)

    @allure.step
    def update_first_name_field(self):
        return self.fill_field(self.first_name, self.NEW_NAME)

    @allure.step
    def update_age_field(self):
        return self.fill_field(self.age, self.NEW_AGE)

    @allure.step
    def assert_that_first_name_field_is_updated(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_first_name)

    @allure.step
    def assert_that_age_field_is_updated(self):
        return self.assert_that_element_is_displayed_by_xpath(self.result_age)



