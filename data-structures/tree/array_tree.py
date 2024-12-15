from typing import TypeVar
from tree.tree import TreeADT

T = TypeVar('T')

class ArrayBasedTree(TreeADT[T]):
    """Implementation using arrays/lists with indices"""
    def __init__(self):
        self._array = []
        
    # Implement all abstract methods...