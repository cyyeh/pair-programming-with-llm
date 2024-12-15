from typing import TypeVar, Generic, Optional, List
from .heap import HeapADT

T = TypeVar('T')

class MaxHeap(HeapADT[T]):
    """Max Heap implementation where parent is larger than children"""
    
    def __init__(self):
        self._data: List[T] = []
    
    def peek(self) -> Optional[T]:
        return self._data[0] if self._data else None
    
    def push(self, value: T) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)
    
    def pop(self) -> Optional[T]:
        if not self._data:
            return None
        result = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        if self._data:
            self._sift_down(0)
        return result
    
    def _sift_up(self, index: int) -> None:
        parent = (index - 1) // 2
        if index > 0 and self._data[index] > self._data[parent]:
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            self._sift_up(parent)
    
    def _sift_down(self, index: int) -> None:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self._data) and self._data[left] > self._data[largest]:
            largest = left
        if right < len(self._data) and self._data[right] > self._data[largest]:
            largest = right
            
        if largest != index:
            self._data[index], self._data[largest] = self._data[largest], self._data[index]
            self._sift_down(largest)
