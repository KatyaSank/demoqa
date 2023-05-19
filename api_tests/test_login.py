from api_methods.Login import *
from pytest import mark


@allure.title('Login with valid data')
def test_valid_login():
    login = Login()
    response = login.login_with_valid_data()
    login.assert_that_token_type_is_str(response)
    login.assert_that_expires_type_is_str(response)
    login.assert_that_status_type_is_str(response)
    login.assert_that_result_type_is_str(response)
    login.assert_status_value(response)
    login.assert_result_value(response)
    login.assert_status_code_200(response)


@allure.title('Login with invalid/incorrect data')
@mark.parametrize('credentials, response', USER_INVALID_DATA)
def test_invalid_login(credentials, response):
    login = Login()
    response = login.login_with_invalid_data(credentials)
    login.assert_message_value(response)
    login.assert_status_code_400(response)
