from typing import TypeVar, Generic

from stack.stack import Stack

# Generic type for stack elements
T = TypeVar('T')


# Example Implementation using Linked List
class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next = None

class LinkedStack(Stack[T]):
    """Linked list-based implementation of Stack ADT"""
    
    def __init__(self):
        self._head = None
        self._size = 0
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def push(self, item: T) -> None:
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
    
    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self._head.data
        self._head = self._head.next
        self._size -= 1
        return item
    
    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._head.data
    
    def size(self) -> int:
        return self._size
