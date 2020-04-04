import heapq
from statistics import median
import sys

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._minheap = [] # heap with max elements, min at the root 
        self._maxheap = [] # heap with min elements, max at the root (everything must be neg)
        self._buffer = []

            
    def addNum(self, num: int) -> None:
        if self._buffer is None:
            if num < (-1) * self._maxheap[0]: # if num is on the left
                heapq.heappush(self._maxheap, (-1) * num)
            else:
                heapq.heappush(self._minheap, num)
            self._balance()
        elif len(self._buffer) < 2:
            self._buffer.append(num)
        elif len(self._buffer) == 2:
            self._minheap.append(max(self._buffer))
            self._maxheap.append((-1)* min(self._buffer))
            self._buffer = None
            self.addNum(num)
            

    def findMedian(self) -> float:
        if self._buffer is None:
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
            heapq.heappush(self._minheap, (-1) *tmp)
        elif len(self._maxheap) < len(self._minheap):
            tmp = heapq.heappop(self._minheap)
            heapq.heappush(self._maxheap, (-1) *tmp)
			
if __name__ == '__main__':
    mf = MedianFinder()
    while True:
        inp = input()
        mf.addNum(int(inp))
        print('Median ', mf.findMedian())
        print('Minheap ',mf._minheap)
        print('Maxheap ',mf._maxheap)
        print('Buffer ',mf._buffer)
		
			