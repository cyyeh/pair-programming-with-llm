from typing import TypeVar, Optional, List
from .balanced_tree import BalancedTreeADT
from .bst import BinarySearchTree, BSTNode

T = TypeVar('T')

class BalancedBSTNode(BSTNode[T]):
    """Node for balanced BST with height information"""
    def __init__(self, value: T):
        super().__init__(value)
        self.height: int = 1
        self.left: Optional[BalancedBSTNode[T]] = None
        self.right: Optional[BalancedBSTNode[T]] = None
        self.parent: Optional[BalancedBSTNode[T]] = None

class BalancedBST(BinarySearchTree[T], BalancedTreeADT[T]):
    """
    Balanced Binary Search Tree implementation
    This is an AVL tree implementation as an example of a balanced BST
    """
    
    def __init__(self):
        super().__init__()
        self._root: Optional[BalancedBSTNode[T]] = None
    
    def get_height(self, value: T) -> int:
        node = self._find_node(value)
        return node.height if node else 0
    
    def update_height(self, value: T) -> None:
        node = self._find_node(value)
        if node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0
            node.height = max(left_height, right_height) + 1
    
    def balance_factor(self, value: T) -> int:
        """Get balance factor of a node (left height - right height)"""
        node = self._find_node(value)
        if not node:
            return 0
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return left_height - right_height
    
    def is_balanced(self) -> bool:
        """Check if the tree is balanced (AVL property)"""
        def check_balance(node: Optional[BalancedBSTNode[T]]) -> bool:
            if not node:
                return True
            balance = self.balance_factor(node.value)
            return -1 <= balance <= 1 and check_balance(node.left) and check_balance(node.right)
        return check_balance(self._root)
    
    def rotate_left(self, value: T) -> None:
        """Perform left rotation"""
        node = self._find_node(value)
        if not node or not node.right:
            return
        
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node
        new_root.parent = node.parent
        
        if not node.parent:
            self._root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
            
        new_root.left = node
        node.parent = new_root
        
        # Update heights
        self.update_height(node.value)
        self.update_height(new_root.value)
    
    def rotate_right(self, value: T) -> None:
        """Perform right rotation"""
        node = self._find_node(value)
        if not node or not node.left:
            return
        
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node
        new_root.parent = node.parent
        
        if not node.parent:
            self._root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
            
        new_root.right = node
        node.parent = new_root
        
        # Update heights
        self.update_height(node.value)
        self.update_height(new_root.value)
    
    def rebalance(self) -> None:
        """Rebalance the entire tree"""
        def rebalance_node(node: Optional[BalancedBSTNode[T]]) -> None:
            if not node:
                return
                
            # Rebalance children first
            rebalance_node(node.left)
            rebalance_node(node.right)
            
            # Update height
            self.update_height(node.value)
            
            # Get balance factor
            balance = self.balance_factor(node.value)
            
            # Left heavy
            if balance > 1:
                # Left-Right case
                if self.balance_factor(node.left.value) < 0:
                    self.rotate_left(node.left.value)
                # Left-Left case
                self.rotate_right(node.value)
            
            # Right heavy
            elif balance < -1:
                # Right-Left case
                if self.balance_factor(node.right.value) > 0:
                    self.rotate_right(node.right.value)
                # Right-Right case
                self.rotate_left(node.value)
        
        rebalance_node(self._root)
    
    def insert(self, value: T, parent_value: Optional[T] = None) -> None:
        """Insert a value and maintain balance"""
        super().insert(value)
        self.rebalance()
    
    def remove(self, value: T) -> None:
        """Remove a value and maintain balance"""
        super().remove(value)
        self.rebalance()