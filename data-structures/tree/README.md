```python
"""
Operation complexities for different tree structures
"""
# Heap
heap_ops = {
    "find_max": "O(1)",
    "insert": "O(log n)",
    "delete_max": "O(log n)",
    "search": "O(n)",  # Not designed for searching
}

# AVL Tree
avl_ops = {
    "search": "O(log n)",
    "insert": "O(log n)",
    "delete": "O(log n)",
    "balance_overhead": "High",
}

# Red-Black Tree
rb_ops = {
    "search": "O(log n)",
    "insert": "O(log n)",
    "delete": "O(log n)",
    "balance_overhead": "Medium",
}

# Splay Tree
splay_ops = {
    "search": "O(log n) amortized",
    "insert": "O(log n) amortized",
    "delete": "O(log n) amortized",
    "balance_overhead": "Low",
}
```