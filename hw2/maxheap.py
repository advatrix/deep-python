from typing import List
from math import floor
 
class MaxHeap:
    def __init__(self) -> None:
        self._heap = []
		
    def push(self, val: int) -> None:
        self._heap.append(val)
        self.heapify(self._heap)

    def pop(self) -> int:
        if not len(self._heap):
            return
        if len(self._heap) == 1:
            return self._heap.pop()
        ret = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.heapify(self._heap)
        return ret

    def heapify(self, iterable: List[int]) -> None:
        for i in range(floor(len(iterable) / 2), -1, -1):
        	MaxHeap._heapify(iterable, i)
            
    @staticmethod
    def left(i: int) -> int:
        return 2 * i + 1
    
    @staticmethod
    def right(i: int) -> int:
        return 2 * i + 2
    
    @staticmethod
    def parent(i: int) -> int:
        return floor((i + 1)/ 2) - 1
    
    @staticmethod
    def _heapify(heap: List[int], i: int) -> None:
        l = MaxHeap.left(i)
        r = MaxHeap.right(i)
        largest = 0
        if l <= len(heap) - 1 and heap[l] > heap[i]:
            largest = l
        else:
            largest = i
        if r <= len(heap) - 1 and heap[r] > heap[largest]:
            largest = r
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            MaxHeap._heapify(heap, largest)

            
if __name__ == '__main__':
    heap = MaxHeap()
    while True:
        print('''
        1 append
        2 pop'''
             )
        a = int(input())
        if a == 1:
            b = int(input())
            heap.push(b)
            print(heap._heap)
        else:
            heap.pop()
            print(heap._heap)
    