"""
Created on Feb 10 00:05:25 2022
"""


class BaseErrorClass(Exception):
    pass


class NonCompliantInputUnits(BaseErrorClass):
    pass


def raise_error(separator, units):
    raise NonCompliantInputUnits(f'Units must be one of {separator.join(units)} (case-insensitive')
