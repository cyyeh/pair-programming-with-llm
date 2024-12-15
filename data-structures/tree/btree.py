from typing import TypeVar, List, Optional, Generic
from abc import abstractmethod
from .tree import TreeADT

T = TypeVar('T')

class BTreeNode(Generic[T]):
    """Base node structure for B-tree variants"""
    def __init__(self, leaf: bool = True):
        self.keys: List[T] = []
        self.children: List[BTreeNode[T]] = []
        self.leaf = leaf
        self.parent: Optional[BTreeNode[T]] = None

class BTree(TreeADT[T], Generic[T]):
    """Basic B-tree implementation"""
    
    def __init__(self, order: int):
        """Initialize B-tree with minimum degree (order)"""
        self.order = order
        self.root: Optional[BTreeNode[T]] = None
    
    def insert(self, value: T, parent_value: Optional[T] = None) -> None:
        if not self.root:
            self.root = BTreeNode[T](True)
            self.root.keys.append(value)
            return
        
        if len(self.root.keys) == (2 * self.order - 1):
            # Split root if full
            new_root = BTreeNode[T](False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        
        self._insert_non_full(self.root, value)
    
    def _split_child(self, parent: BTreeNode[T], index: int) -> None:
        """Split a full child node"""
        order = self.order
        child = parent.children[index]
        new_node = BTreeNode[T](child.leaf)
        
        # Move keys and children
        parent.keys.insert(index, child.keys[order - 1])
        parent.children.insert(index + 1, new_node)
        
        new_node.keys = child.keys[order:]
        child.keys = child.keys[:order - 1]
        
        if not child.leaf:
            new_node.children = child.children[order:]
            child.children = child.children[:order]
    
    def _insert_non_full(self, node: BTreeNode[T], value: T) -> None:
        """Insert into a non-full node"""
        i = len(node.keys) - 1
        
        if node.leaf:
            # Insert into leaf node
            while i >= 0 and value < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, value)
        else:
            # Recursively insert into appropriate child
            while i >= 0 and value < node.keys[i]:
                i -= 1
            i += 1
            
            if len(node.children[i].keys) == (2 * self.order - 1):
                self._split_child(node, i)
                if value > node.keys[i]:
                    i += 1
            
            self._insert_non_full(node.children[i], value)
