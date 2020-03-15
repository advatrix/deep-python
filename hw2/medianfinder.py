import heapq
from statistics import median

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
		self._minheap = []
		self._maxheap = []
		self._buffer = []

    def addNum(self, num: int) -> None:
        if len(self._buffer) < 2:
			self._buffer.append(num)
		elif len(self._buffer) == 2:
			self._minheap.append(max(self._buffer))
			self._maxheap.append(min(self._buffer))
		else:
			if num < -self._maxheap[0]:
				heapq.heappush(self._maxheap, -num)
			else:
				heapq.heappush(self._minheap, num)
			self._balance()

    def findMedian(self) -> float:
		if len(self._buffer) > 2:
			if len(self._minheap) == len(self._maxheap):
				return (self._minheap[0] - self._maxheap[0]) / 2
			elif len(self._minheap) > len(self._maxheap):
				return self._minheap[0]
			else:
				return -self._maxheap[0]
		else:
			return median(self._buffer)
	
	def _balance(self):
		if len(self._maxheap) > len(self._minheap):
			tmp = heapq.heappop(self._maxheap)
			heapq.heappush(self._minheap, -tmp)
		elif len(self._minheap) > len(self._minheap):
			tmp = heapq.heappop(self._minheap)
			heapq.heappush(self._maxheap, -tmp)
			
if __name__ == '__main__':
	mf = MedianFinder()
	for inp in sys.stdin:
		mf.addNum(int(inp))
		print(mf.findMedian)
		print(mf._minheap)
		print(mf._maxheap)
		print(mf._buffer)
		
			