from typing import TypeVar, Optional, List, Generic
from .tree import TreeADT

T = TypeVar('T')

class BSTNode(Generic[T]):
    """Binary Search Tree node"""
    def __init__(self, value: T):
        self.value: T = value
        self.left: Optional[BSTNode[T]] = None
        self.right: Optional[BSTNode[T]] = None
        self.parent: Optional[BSTNode[T]] = None

class BinarySearchTree(TreeADT[T], Generic[T]):
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self._root: Optional[BSTNode[T]] = None
        self._size: int = 0
    
    def is_empty(self) -> bool:
        return self._root is None
    
    def root(self) -> Optional[T]:
        return self._root.value if self._root else None
    
    def _find_node(self, value: T) -> Optional[BSTNode[T]]:
        """Helper method to find a node by value"""
        current = self._root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return None
    
    def parent(self, value: T) -> Optional[T]:
        node = self._find_node(value)
        if node and node.parent:
            return node.parent.value
        return None
    
    def children(self, value: T) -> List[T]:
        node = self._find_node(value)
        if not node:
            return []
        children = []
        if node.left:
            children.append(node.left.value)
        if node.right:
            children.append(node.right.value)
        return children
    
    def is_leaf(self, value: T) -> bool:
        node = self._find_node(value)
        return node is not None and node.left is None and node.right is None
    
    def insert(self, value: T, parent_value: Optional[T] = None) -> None:
        """
        Insert a new value into the BST.
        Note: parent_value is ignored as BST determines position based on value
        """
        new_node = BSTNode(value)
        
        if self.is_empty():
            self._root = new_node
            self._size += 1
            return
        
        current = self._root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
        
        self._size += 1
    
    def remove(self, value: T) -> None:
        node = self._find_node(value)
        if not node:
            raise ValueError(f"Value {value} not found in tree")
        
        self._size -= 1
        
        # Case 1: Node has no children
        if not node.left and not node.right:
            self._remove_leaf(node)
        
        # Case 2: Node has one child
        elif not node.left:
            self._replace_node(node, node.right)
        elif not node.right:
            self._replace_node(node, node.left)
        
        # Case 3: Node has two children
        else:
            # Find successor (smallest value in right subtree)
            successor = self._find_min(node.right)
            node.value = successor.value
            if successor.parent == node:
                self._replace_node(successor, successor.right)
            else:
                self._replace_node(successor, successor.right)
    
    def _remove_leaf(self, node: BSTNode[T]) -> None:
        """Helper method to remove a leaf node"""
        if node.parent:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        else:
            self._root = None
    
    def _replace_node(self, node: BSTNode[T], replacement: Optional[BSTNode[T]]) -> None:
        """Helper method to replace a node with another node"""
        if node.parent:
            if node.parent.left == node:
                node.parent.left = replacement
            else:
                node.parent.right = replacement
        else:
            self._root = replacement
        
        if replacement:
            replacement.parent = node.parent
    
    def _find_min(self, node: BSTNode[T]) -> BSTNode[T]:
        """Helper method to find the minimum value in a subtree"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def size(self) -> int:
        return self._size
    
    def height(self) -> int:
        def calculate_height(node: Optional[BSTNode[T]]) -> int:
            if not node:
                return -1
            return 1 + max(calculate_height(node.left), calculate_height(node.right))
        
        return calculate_height(self._root)
    
    def find(self, value: T) -> bool:
        """Search for a value in the BST"""
        return self._find_node(value) is not None
    
    def min_value(self) -> Optional[T]:
        """Find the minimum value in the BST"""
        if not self._root:
            return None
        return self._find_min(self._root).value
    
    def max_value(self) -> Optional[T]:
        """Find the maximum value in the BST"""
        if not self._root:
            return None
        current = self._root
        while current.right:
            current = current.right
        return current.value
    
    def inorder_traversal(self) -> List[T]:
        """Return sorted list of values (inorder traversal)"""
        result = []
        
        def inorder(node: Optional[BSTNode[T]]) -> None:
            if not node:
                return
            inorder(node.left)
            result.append(node.value)
            inorder(node.right)
        
        inorder(self._root)
        return result
    
    def __str__(self) -> str:
        """Return string representation of the BST"""
        if self.is_empty():
            return "Empty BST"
        
        lines = []
        def print_tree(node: Optional[BSTNode[T]], level: int = 0, prefix: str = "Root: "):
            if not node:
                return
            lines.append("  " * level + prefix + str(node.value))
            if node.left or node.right:
                if node.left:
                    print_tree(node.left, level + 1, "L--- ")
                if node.right:
                    print_tree(node.right, level + 1, "R--- ")
        
        print_tree(self._root)
        return "\n".join(lines)


if __name__ == "__main__":
    # Create a BST
    bst = BinarySearchTree[int]()

    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)

    # Print the tree structure
    print(bst)
    # Output:
    # Root: 50
    #   L--- 30
    #     L--- 20
    #     R--- 40
    #   R--- 70
    #     L--- 60
    #     R--- 80

    # Basic operations
    print(bst.size())               # 7
    print(bst.height())            # 2
    print(bst.find(40))           # True
    print(bst.find(90))           # False
    print(bst.min_value())        # 20
    print(bst.max_value())        # 80
    print(bst.inorder_traversal()) # [20, 30, 40, 50, 60, 70, 80]

    # Remove a node
    bst.remove(30)
    print(bst)
    # Output:
    # Root: 50
    #   L--- 40
    #     L--- 20
    #   R--- 70
    #     L--- 60
    #     R--- 80