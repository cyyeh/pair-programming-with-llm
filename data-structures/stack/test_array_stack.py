import pytest

from stack.array_stack import ArrayStack

@pytest.fixture
def empty_stack():
    """Fixture that returns an empty stack"""
    return ArrayStack()

@pytest.fixture
def stack_with_items():
    """Fixture that returns a stack with some items"""
    stack = ArrayStack()
    items = [1, 2, 3]
    for item in items:
        stack.push(item)
    return stack

def test_new_stack_is_empty(empty_stack):
    """Test that a newly created stack is empty"""
    assert empty_stack.is_empty()
    assert empty_stack.size() == 0

def test_push_to_empty_stack(empty_stack):
    """Test pushing an item to an empty stack"""
    empty_stack.push(1)
    assert not empty_stack.is_empty()
    assert empty_stack.size() == 1
    assert empty_stack.peek() == 1

def test_push_multiple_items(empty_stack):
    """Test pushing multiple items to a stack"""
    items = [1, 2, 3]
    for item in items:
        empty_stack.push(item)
    assert empty_stack.size() == 3
    assert empty_stack.peek() == 3

def test_pop_from_stack(stack_with_items):
    """Test popping items from a stack"""
    assert stack_with_items.pop() == 3
    assert stack_with_items.size() == 2
    assert stack_with_items.peek() == 2

def test_peek_stack(stack_with_items):
    """Test peeking at top item without removing it"""
    assert stack_with_items.peek() == 3
    assert stack_with_items.size() == 3  # Size shouldn't change

def test_pop_until_empty(stack_with_items):
    """Test popping all items until stack is empty"""
    while not stack_with_items.is_empty():
        stack_with_items.pop()
    assert stack_with_items.is_empty()
    assert stack_with_items.size() == 0

def test_pop_empty_stack(empty_stack):
    """Test that popping from empty stack raises exception"""
    with pytest.raises(IndexError):
        empty_stack.pop()

def test_peek_empty_stack(empty_stack):
    """Test that peeking at empty stack raises exception"""
    with pytest.raises(IndexError):
        empty_stack.peek()


def test_stack_maintains_order(empty_stack):
    """Test that stack maintains LIFO order"""
    items = [1, 2, 3, 4]
    for item in items:
        empty_stack.push(item)
    
    for item in reversed(items):
        assert empty_stack.pop() == item
