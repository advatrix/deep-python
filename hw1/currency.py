#! /usr/bin/env python

class Currency():
	
	def __init__(self, value, currency='CU'):
		self._value = value
		self._cu = currency
		if self._cu == 'CU' or self._cu == 'RUR':
			self._cc = 1
		elif self._cu == 'USD':
			self._cc = 68.77
		elif self._cu == 'EUR':
			self._cc = 77.92
		elif self._cu == 'CNY':
			self._cc = 9.92
		elif self._cu == 'UAH':
			self._cc = 2.75
		
	def __add__(self, other):
		if isinstance(other, int):
			return Currency(self._value + other, self._cu)
		else:
			return Currency((self._value * self._cc + other._value * other._cc) / self._cc, self._cu)
		
	def __sub__(self, other):
		if isinstance(other, int):
			return Currency(self._value - other, self._cu)
		else:
			return Currency((self._value * self._cc - other._value * other._cc) / self._cc, self._cu)
		
	def __mul__(self, other):
		if isinstance(other, int):
			return Currency(self._value * other, self._cu)
		else:
			return Currency((self._value * self._cc * other._value * other._cc) / self._cc, self._cu)

	def __div__(self, other):
		if isinstance(other, int):
			return Currency(self._value // other, self._cu)
		else:
			return Currency(((self._value * self._cc) // (other._value * other._cc)) / self._cc, self._cu)
	
	def __truediv__(self, other):
		if isinstance(other, int):
			return Currency(self._value / other, self._cu)
		else:
			return Currency((self._value * self._cc / other._value * other._cc) / self._cc, self._cu)
		
	def __str__(self):
		return self._cu+' '+str(self._value)
	
	def __repr__(self):
		return 'Currency: '+ self._cu + '\nValue: '+ str(self._value)
		
	