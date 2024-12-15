from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Generic type for stack elements
T = TypeVar('T')

class Stack(ABC, Generic[T]):
    """Abstract Stack ADT"""
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if stack is empty"""
        pass
    
    @abstractmethod
    def push(self, item: T) -> None:
        """Add item to top of stack"""
        pass
    
    @abstractmethod
    def pop(self) -> T:
        """Remove and return top item from stack"""
        pass
    
    @abstractmethod
    def peek(self) -> T:
        """Return top item without removing it"""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Return number of items in stack"""
        pass
