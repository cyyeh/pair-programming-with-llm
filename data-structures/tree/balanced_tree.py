from abc import abstractmethod
from typing import TypeVar, Generic, Optional
from tree.tree import TreeADT

T = TypeVar('T')

class BalancedTreeADT(TreeADT[T], Generic[T]):
    """Abstract base class for balanced tree data structures"""
    
    @abstractmethod
    def balance_factor(self, value: T) -> int:
        """
        Calculate the balance factor of a node
        Returns difference in height between left and right subtrees
        """
        pass
    
    @abstractmethod
    def rebalance(self) -> None:
        """Rebalance the entire tree if needed"""
        pass
    
    @abstractmethod
    def rotate_left(self, value: T) -> None:
        """Perform a left rotation on the given node"""
        pass
    
    @abstractmethod
    def rotate_right(self, value: T) -> None:
        """Perform a right rotation on the given node"""
        pass
    
    @abstractmethod
    def is_balanced(self) -> bool:
        """Check if the tree is balanced according to the implementation's criteria"""
        pass
    
    @abstractmethod
    def get_height(self, value: T) -> int:
        """Get the height of a specific node"""
        pass
    
    @abstractmethod
    def update_height(self, value: T) -> None:
        """Update the height of a specific node"""
        pass
    
    def insert(self, value: T, parent_value: Optional[T] = None) -> None:
        """
        Override insert to ensure tree remains balanced
        Implementations should call super().insert() and then rebalance
        """
        super().insert(value, parent_value)
        self.rebalance()
    
    def remove(self, value: T) -> None:
        """
        Override remove to ensure tree remains balanced
        Implementations should call super().remove() and then rebalance
        """
        super().remove(value)
        self.rebalance() 