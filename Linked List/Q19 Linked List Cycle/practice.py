# My Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Correct Solution
# Time: O(n) | Space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Correct Solution 2
# Time: O(n) | Space: O(n)
class Solution2:
    def hasCycle(self, head:ListNode):
        pointer = head
        visited = set()
        while pointer:
            if pointer in visited:
                return True
            else:
                visited.add(pointer)
            pointer = pointer.next
        return False
