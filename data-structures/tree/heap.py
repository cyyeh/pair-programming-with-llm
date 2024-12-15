from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List
from .balanced_tree import BalancedTreeADT

T = TypeVar('T')

class HeapADT(ABC, Generic[T]):
    """Abstract base class for Heap data structure"""
    
    @abstractmethod
    def peek(self) -> Optional[T]:
        """Return the root element without removing it"""
        pass
    
    @abstractmethod
    def push(self, value: T) -> None:
        """Add an element to the heap"""
        pass
    
    @abstractmethod
    def pop(self) -> Optional[T]:
        """Remove and return the root element"""
        pass
    
    @abstractmethod
    def heapify(self, values: List[T]) -> None:
        """Build heap from a list of values"""
        pass
