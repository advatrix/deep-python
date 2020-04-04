from typing import List
 
class MaxHeap:
    def __init__(self) -> None:
        self._heap = []
		
    def push(self, val: int) -> None:
        self._heap.append(val)
        self.heapify(self._heap)

    def pop(self) -> int:
        ret = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.heapify(self._heap)
        return ret

    def heapify(self, iterable: List[int]) -> None:
        for i in range(len(iterable) // 2, 1, -1):
        	self._heapify(iterable, i)
			
    @staticmethod
    def _heapify(iterable: List[int], idx: int) -> None:
        left = 2 * idx
        right = 2 * idx + 1
        largest = idx
        if left <= len(iterable) and iterable[left] > iterable[largest]:
            largest = left
        if right <= len(iterable) and iterable[right] > iterable[largest]:
            largest = right
        if largest != idx:
            iterable[largest], iterable[idx] = iterable[idx], iterable[largest]
            self._heapify(iterable, largest)
            
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
    