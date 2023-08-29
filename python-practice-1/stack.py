class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._top.item

    def push(self, item):
        """Method to push an item to the top of a Stack"""
        new_node = _StackNode(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """Method to pop an item from the top of a Stack"""
        assert not self.is_empty(), "Cannot pop from an empty stack"
        popped_item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return popped_item

    def __len__(self):
        """Overrides the Python len() method for Stack objects"""
        return self._size

    def is_empty(self):
        """Used to tell us whether the Stack is empty (returns a True or False)"""
        return self._size == 0

# # Inline unittest
# import unittest

# class TestStack(unittest.TestCase):
#     def test_push(self):
#         stack = Stack()
#         stack.push(5)
#         self.assertEqual(stack.peek(), 5)
#         stack.push(10)
#         self.assertEqual(stack.peek(), 10)

#     def test_pop(self):
#         stack = Stack()
#         stack.push(5)
#         stack.push(10)
#         self.assertEqual(stack.pop(), 10)
#         self.assertEqual(stack.pop(), 5)
#         with self.assertRaises(AssertionError):
#             stack.pop()

#     def test_len(self):
#         stack = Stack()
#         self.assertEqual(len(stack), 0)
#         stack.push(5)
#         self.assertEqual(len(stack), 1)
#         stack.push(10)
#         self.assertEqual(len(stack), 2)
#         stack.pop()
#         self.assertEqual(len(stack), 1)
#         stack.pop()
#         self.assertEqual(len(stack), 0)

#     def test_is_empty(self):
#         stack = Stack()
#         self.assertTrue(stack.is_empty())
#         stack.push(5)
#         self.assertFalse(stack.is_empty())
#         stack.pop()
#         self.assertTrue(stack.is_empty())

# if __name__ == "__main__":
#     unittest.main()
