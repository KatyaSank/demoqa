from pytest import mark
from api_methods.Registration import *


def test_positive():
    registration = Registration()
    response = registration.registration_with_valid_data()
    # user_id = response.json().get('userID')
    # print(user_id)
    registration.assert_that_userid_type_is_str(response)
    registration.assert_that_username_type_is_str(response)
    registration.assert_status_code_201(response)


@mark.parametrize('x, response', REGISTRATION_INVALID_DATA)
def test_negative(x, response):
    registration = Registration()
    response = registration.registration_with_invalid_data(x)
    registration.assert_status_code_400(response)
    registration.assert_message_value(response)


