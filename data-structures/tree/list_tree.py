from typing import TypeVar, Generic
from tree.tree import TreeADT

T = TypeVar('T')

class ListBasedTree(TreeADT[T]):
    """Implementation using lists"""
    def __init__(self):
        self._nodes = []
        
    # Implement all abstract methods...
