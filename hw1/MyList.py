#! /usr/bin/env python

class MyList(list):
	
	def __add__(self, other):
		if len(self) == len(other):
			return [self[i] + other[i] for i in range(len(self))]
		elif len(self) < len(other):
			app = [self[i] for i in range(len(self))] + [0] * (len(other) - len(self))
			return [app[i] + other[i] for i in range(len(other))]
		else:
			app = [other[i] for i in range(len(other))] + [0] * (len(self) - len(other))
			return [self[i] + app[i] for i in range(len(self))]
		
	def __iadd__(self, other):
		self = self + other
		return self
		
	def __sub__(self, other):
		if len(self) == len(other):
			return [self[i] - other[i] for i in range(len(self))]
		elif len(self) < len(other):
			app = [self[i] for i in range(len(self))] + [0] * (len(other) - len(self))
			return [app[i] - other[i] for i in range(len(other))]
		else:
			app = [other[i] for i in range(len(other))] + [0] * (len(self) - len(other))
			return [self[i] - app[i] for i in range(len(self))]
		
	def __lt__(self, other):
		return sum(self) < sum(other)
	
	def __le__(self, other):
		return sum(self) <= sum(other)
	
	def __eq__(self, other):
		return sum(self) == sum(other)
	
	def __ge__(self, other):
		return sum(self) >= sum(other)
	
	def __gt__(self, other):
		return sum(self) > sum(other)
	
	def __ne__(self, other):
		return sum(self) != sum(other)
