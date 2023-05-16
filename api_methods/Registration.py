import allure
from api_methods.BaseMethods import Base
import random

UPPER = 'EYUIOA'
LOWER = 'qwrtpsdfghjklzxcvbnm'
NUMBER = '1234567890'
SYMBOLS = '!@#$%&*?'

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


def login(length):
    return ''.join(list([random.choice(UPPER + LOWER) for i in range(length)]))


def passwd(length):
    return ''.join(list([random.choice(UPPER + LOWER + NUMBER + SYMBOLS) for i in range(length)]))


class Registration(Base):
    def __init__(self):
        self.url = 'https://demoqa.com/Account/v1/User'
        self.user = {"userName": f"{login(8)}", "password": f"{passwd(20)}"}
        self.userID = 'userID'
        self.username = 'username'
        self.message = 'message'
        self.message_text = 'UserName and Password required.'

    @allure.step
    def registration_with_valid_data(self):
        return self.post(self.url, self.user)

    @allure.step
    def registration_with_invalid_data(self, x):
        return self.post(self.url, x)

    @allure.step
    def assert_that_userid_type_is_str(self, response):
        return self.assert_str_type(response, self.userID)

    @allure.step
    def assert_that_username_type_is_str(self, response):
        return self.assert_str_type(response, self.username)

    @allure.step
    def assert_message_value(self, response):
        return self.assert_value_of_parameter(response, self.message, self.message_text)

    @allure.step
    def assert_status_code_201(self, response):
        return self.assert_status_code(response, 201)

    @allure.step
    def assert_status_code_400(self, response):
        return self.assert_status_code(response, 400)
