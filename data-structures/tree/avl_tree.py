from typing import TypeVar, Optional
from .balanced_tree import BalancedTreeADT, Node

T = TypeVar('T')

class AVLNode(Node[T]):
    """AVL Tree node with height information"""
    def __init__(self, value: T):
        super().__init__(value)
        self.height: int = 1

class AVLTree(BalancedTreeADT[T]):
    """AVL Tree implementation"""
    def __init__(self):
        self._root: Optional[AVLNode[T]] = None
    
    # Implement other abstract methods... 