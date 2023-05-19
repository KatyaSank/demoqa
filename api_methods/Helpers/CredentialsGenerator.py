import random

UPPER = 'EYUIOA'
LOWER = 'qwrtpsdfghjklzxcvbnm'
NUMBER = '1234567890'
SYMBOLS = '!@#$%&*?'


class Credentials:
    @staticmethod
    def login(length):
        return ''.join(list([random.choice(UPPER + LOWER) for i in range(length)]))

    @staticmethod
    def passwd(length):
        return ''.join(list([random.choice(UPPER + LOWER + NUMBER + SYMBOLS) for i in range(length)]))
