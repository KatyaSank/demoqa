import allure
from api_methods.BaseMethods import BaseApiMethod
from api_methods.Helpers.CredentialsGenerator import *

REGISTRATION_INVALID_DATA = ({"userName": "", "password": ""},
                             {"userName": "", "password": "Qwerty12345!@#$%"},
                             {"userName": "KatyaSank", "password": ""},
                             {"key": "", "key2": ""},
                             {"userName": "KatyaSank", "password": "1234567"},
                             {"userName": "KatyaSank", "password": "        "},
                             {"userName": "KatyaSank", "password": "qwertyuio"},
                             {"userName": "KatyaSank", "password": "1234567"},
                             {"userName": "KatyaSank", "password": "QWERTY!@#$%^1234"},
                             {"userName": "KatyaSank", "password": "Qwerty1%"})


class Registration(BaseApiMethod, Credentials):
    def __init__(self):
        self.url = 'https://demoqa.com/Account/v1/User'
        self.user = {"userName": f"{self.login(8)}", "password": f"{self.passwd(20)}"}
        self.userID = 'userID'
        self.username = 'username'
        self.message = 'message'
        self.message_text = 'UserName and Password required.'

    @allure.step("Registration with correct data")
    def registration_with_valid_data(self):
        return self.post(self.url, self.user)

    @allure.step("Registration with invalid data")
    def registration_with_invalid_data(self, x):
        return self.post(self.url, x)

    @allure.step("Check that userid has correct data type")
    def assert_that_userid_type_is_str(self, response):
        return self.assert_str_type(response, self.userID)

    @allure.step("Check that username has correct data type")
    def assert_that_username_type_is_str(self, response):
        return self.assert_str_type(response, self.username)

    @allure.step("Check that message has correct value")
    def assert_message_value(self, response):
        return self.assert_value_of_parameter(response, self.message, self.message_text)

    @allure.step("Check that status code is 201")
    def assert_status_code_201(self, response):
        return self.assert_status_code(response, 201)

    @allure.step("Check that status code is 400")
    def assert_status_code_400(self, response):
        return self.assert_status_code(response, 400)
