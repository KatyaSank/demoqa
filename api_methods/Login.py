import allure
from api_methods.BaseMethods import BaseApiMethod


USER_INVALID_DATA = ({"userName": "", "password": ""},
                     {"userName": "", "password": "Qwerty12345!@#$%"},
                     {"userName": "KatyaSank", "password": ""},
                     {"key": "", "key2": ""},
                     {"userName": "KatyaSank", "password": "1234567"},
                     {"userName": "KatyaSank", "password": "        "},
                     {"userName": "KatyaSank", "password": "qwertyuio"},
                     {"userName": "KatyaSank", "password": "1234567"},
                     {"userName": "Katya", "password": "Qwerty12345!@#$%"},
                     {"userName": "KatyaSank", "password": "Qwerty1%"})


class Login(BaseApiMethod):
    def __init__(self):
        self.url = 'https://demoqa.com/Account/v1/GenerateToken'
        self.user = {"userName": "Katerina", "password": "Qwerty123!@#$."}
        self.token = 'token'
        self.expires = 'expires'
        self.status = 'status'
        self.result = 'result'
        self.status_text = 'Success'
        self.result_text = 'User authorized successfully.'
        self.message = 'message'
        self.message_text = 'UserName and Password required.'

    @allure.step("Login with correct data")
    def login_with_valid_data(self):
        return self.post(self.url, self.user)

    @allure.step("Login with invalid data")
    def login_with_invalid_data(self, credentials):
        return self.post(self.url, credentials)

    @allure.step("Check that token has correct data type")
    def assert_that_token_type_is_str(self, response):
        return self.assert_str_type(response, self.token)

    @allure.step("Check that expires has correct data type")
    def assert_that_expires_type_is_str(self, response):
        return self.assert_str_type(response, self.expires)

    @allure.step("Check that status has correct data type")
    def assert_that_status_type_is_str(self, response):
        return self.assert_str_type(response, self.status)

    @allure.step("Check that result has correct data type")
    def assert_that_result_type_is_str(self, response):
        return self.assert_str_type(response, self.result)

    @allure.step("Check that status has correct value")
    def assert_status_value(self, response):
        return self.assert_value_of_parameter(response, self.status, self.status_text)

    @allure.step("Check that result has correct value")
    def assert_result_value(self, response):
        return self.assert_value_of_parameter(response, self.result, self.result_text)

    @allure.step("Check that message has correct value")
    def assert_message_value(self, response):
        return self.assert_value_of_parameter(response, self.message, self.message_text)

    @allure.step("Check that status code is 200")
    def assert_status_code_200(self, response):
        return self.assert_status_code(response, 200)

    @allure.step("Check that status code is 400")
    def assert_status_code_400(self, response):
        return self.assert_status_code(response, 400)
