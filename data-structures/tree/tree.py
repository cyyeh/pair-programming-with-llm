from abc import ABC, abstractmethod
from typing import Any, Optional, List, TypeVar, Generic

# Define generic type variable
T = TypeVar('T')

class TreeADT(ABC, Generic[T]):
    """Abstract base class defining the Tree ADT interface"""
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the tree is empty"""
        pass
    
    @abstractmethod
    def root(self) -> Optional[T]:
        """Return the root value of the tree"""
        pass
    
    @abstractmethod
    def parent(self, value: T) -> Optional[T]:
        """Return the parent value of a given node"""
        pass
    
    @abstractmethod
    def children(self, value: T) -> List[T]:
        """Return a list of children values for a given node"""
        pass
    
    @abstractmethod
    def is_leaf(self, value: T) -> bool:
        """Check if a given node is a leaf"""
        pass
    
    @abstractmethod
    def insert(self, value: T, parent_value: Optional[T] = None) -> None:
        """Insert a new value into the tree"""
        pass
    
    @abstractmethod
    def remove(self, value: T) -> None:
        """Remove a value from the tree"""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Return the total number of nodes in the tree"""
        pass
    
    @abstractmethod
    def height(self) -> int:
        """Return the height of the tree"""
        pass

class Node(Generic[T]):
    """Basic tree node structure"""
    def __init__(self, value: T):
        self.value: T = value
        self.children: List[Node[T]] = []
        self.parent: Optional[Node[T]] = None
