from typing import TypeVar

from stack.stack import Stack


# Generic type for stack elements
T = TypeVar('T')

# Example Implementation using List
class ArrayStack(Stack[T]):
    """Array-based implementation of Stack ADT"""
    
    def __init__(self):
        self._items: list[T] = []
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def size(self) -> int:
        return len(self._items)
