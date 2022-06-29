# Name

141 Linked List Cycle

## Problem

* Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## New Topics

* Floyd's Tortoise and Hare algorithim

## Solution

* To understand this problem you need to know Tortoise and Hare algorithim. It involves two pointers fast and slow. Slow moves to the next pointer and fast moves to the pointer after the next pointer. If fast and slow equal the same then the linked list is a cycle and return True. If not then it is not a cycle.

```python
# Time: O(n) | Space: O(n)
class Solution:
    def ll_cycle(self, head):
        point = head
        # you create a pointer
        visited = set()
        # you create a set because set cannot contain duplicates
        while pointer:
        # while there is a head            
            if pointer in visited:
            # if the head is in the visited set
                return True
                # return True
            else:
                visited.add(pointer)
                # else add it in the visited set
            pointer = pointer.next
            # make the pointer equal pointer.next
        return False
        # otherwise return False


# Time: O(n) | Space: O(1)
class Solution2:
    def ll_cycle(self, head:Node):
        slow,fast = head, head
        # used as a starting point

        while fast and fast.next:
        # used to check if there is a head and head.next
            slow = slow.next
            # creates the slow pointer which checks the next node
            fast = fast.next.next
            # creates a fast pointer that checks the node after the next node

            if slow == fast:
            # if the slow node == fast node that means that 
                return True
                # there is a cycle
        return False
        # in any instance other than the while loop it will return False
```