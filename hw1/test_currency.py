import pytest

from currency import Currency

a = Currency(1)
b = Currency(2, 'RUR')
c = Currency(3, 'USD')
d = Currency(4, 'EUR')
e = Currency(5, 'UAH')
f = Currency(6, 'CNY')

def test_add():
	assert((b + a)._value == 3)
	assert((b + a)._cu == 'RUR')
	assert((b + c)._cu == 'RUR')
	assert((b + c)._value == 208.31)
'''
a + a = exception
b + a = curr b'''
