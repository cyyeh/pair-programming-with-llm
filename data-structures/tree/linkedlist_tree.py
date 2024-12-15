from typing import TypeVar
from tree.tree import TreeADT

T = TypeVar('T')

class LinkedTree(TreeADT[T]):
    """Implementation using linked nodes"""
    def __init__(self):
        self._root = None
        
    # Implement all abstract methods...