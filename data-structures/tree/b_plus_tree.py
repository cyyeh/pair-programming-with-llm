from typing import TypeVar, Optional, List
from .btree import BTreeNode, BTree

T = TypeVar('T')

class BPlusTreeNode(BTreeNode[T]):
    """Node structure for B+ tree"""
    def __init__(self, leaf: bool = True):
        super().__init__(leaf)
        self.next: Optional[BPlusTreeNode[T]] = None  # For leaf node linking

class BPlusTree(BTree[T]):
    """B+ tree implementation"""
    
    def __init__(self, order: int):
        super().__init__(order)
        self.root: Optional[BPlusTreeNode[T]] = None
        self._leftmost_leaf: Optional[BPlusTreeNode[T]] = None
    
    def insert(self, value: T, parent_value: Optional[T] = None) -> None:
        if not self.root:
            self.root = BPlusTreeNode[T](True)
            self.root.keys.append(value)
            self._leftmost_leaf = self.root
            return
        
        # Similar to B-tree insert but maintains leaf node links
        # Implementation details...
    
    def range_query(self, start: T, end: T) -> List[T]:
        """Efficient range query using leaf node links"""
        result = []
        leaf = self._find_leaf(start)
        
        while leaf and leaf.keys[0] <= end:
            for key in leaf.keys:
                if start <= key <= end:
                    result.append(key)
            leaf = leaf.next
        
        return result
