import requests


class BaseApiMethod:
    @staticmethod
    def get(url, data):
        return requests.get(url, data)

    @staticmethod
    def post(url, data):
        return requests.post(url, data)

    @staticmethod
    def delete(self, url, method, code):
        self.assert_status_code(method, code)
        return requests.delete(url)

    @staticmethod
    def assert_str_type(method, parameter):
        assert isinstance(method.json().get(parameter), str)

    @staticmethod
    def assert_value_of_parameter(method, parameter, text):
        assert method.json().get(parameter) == text

    @staticmethod
    def assert_status_code(method, code):
        assert method.status_code == code
