from pytest import mark
from api_methods.Registration import *


@allure.title('Registration with valid data')
def test_positive():
    registration = Registration()
    response = registration.registration_with_valid_data()
    registration.assert_that_userid_type_is_str(response)
    registration.assert_that_username_type_is_str(response)
    registration.assert_status_code_201(response)


@allure.title('Registration with invalid/incorrect data')
@mark.parametrize('credentials, response', REGISTRATION_INVALID_DATA)
def test_negative(credentials, response):
    registration = Registration()
    response = registration.registration_with_invalid_data(credentials)
    registration.assert_status_code_400(response)
    registration.assert_message_value(response)
