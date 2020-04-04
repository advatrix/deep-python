import time
from collections import OrderedDict

class ICache:
    def __init__(self, capacity: int=10) -> None:
        # self._heap = [0] * capacity # last times used
		self._storage = OrderedDict()
		self._capacity = capacity
		
    def get(self, key: str) -> str:
		if key in self._storage:
			ret = self._storage[key]
			self._storage.move_to_end(key)
			return ret
		else:
			return None

    def set(self, key: str, value: str) -> None:
        if len(self._storage) == self._capacity:
			self._storage.popitem(last=False)
		self._storage[key] = value

    def del(self, key: str) -> None:
        if key in self._storage:
			del self._storage[key]
    
	def __rrp
		
'''	
class Cashable:
	
	def __init__(self, key: str, value: str):
		self._time = time.time()
		self._key = key
		self._value = value
		
	def update(self):
		self._time = time.time()
		'''


if __name__ == '__main__':
	c = ICache()
	c.set(12, 34)
	c.set(45, 66)
	