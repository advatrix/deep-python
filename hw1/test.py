import pytest
from MyList import MyList


a = MyList([1, 2, 3])
b = MyList([5, 6, 7])
c = MyList([])
d = MyList([1, 2, 3, 4, 5])
e = MyList([3, 3])

def test_add():
	assert(a + b == [6, 8, 10])
	assert(b + a == [6, 8, 10])
	assert(a + c == [1, 2, 3])
	assert(d + e == [4, 5, 3, 4, 5])

def test_sub():
	assert(a - b == [-4, -4, -4])
	assert(a - c == [1, 2, 3])
	assert(d - e == [-2, -1, 3, 4, 5])
	assert(a - d == [0, 0, 0, -4, -5])
	
def test_eq():
	assert(a < b)
	assert(e == e)
	assert(e == a)
	assert(c < a)
	assert(d < b)