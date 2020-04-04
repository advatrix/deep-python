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
            return ''
        
    def delete(self, key: str) -> None:
            if key in self._storage:
                del self._storage[key]

    def set(self, key: str, value: str) -> None:
        if len(self._storage) == self._capacity and key not in self._storage.keys():
            self._storage.popitem(last=False)
        self._storage[key] = value

    def __repr__(self):
        return repr(self._storage)


if __name__ == '__main__':
    c = ICache(3)
    print(repr(c))
    c.set(12, 34)
    print(repr(c))
    c.set(45, 66)
    print(repr(c))
    print(c.get(12))
    print(repr(c))
    c.set(16, 32)
    print(c)
    c.set(19, 21)
    print(c)
    print(c.get(45))
    c.delete(55)
    print(c)
    c.delete(16)
    print(c)