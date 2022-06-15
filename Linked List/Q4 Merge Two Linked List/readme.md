# Name

Merge Two Linked List

## Problem

* You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Solution

```python
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def Solution(list1, list2):
    dummy = ListNode()
    # we create a dummy node as a place holder to be able to traverse the list
    tail = dummy
    # we save the dummy value in the tail variable

    while list1 and list2:
    # as long as both list1 and list2 have a head
        if list1.val <= list2.val:
        # we check to see if the node in list1 is less than or equal to the node in list 2
            tail.next = list1
            #if it is less than or equal to list2 then we save listl node in tail.next because the dummy.val is 0 but the next node is none
            list1 = list1.next
            # we then increase the iteration by having list1 = list1.next
        else:
            tail.next = list2
            # if list2.val is <= list1.val we make the tail.next = list2 node
            list2 = list2.next
            # we increase the list2 to iterate through the nodes by making list2 = list2.next
        tail = tail.next
        # you use this to continue iterating through the tail list for each node in list1 and list2
    if list1:
    # this is triggered when either list1 or list2 is at None
    # in this situation if there is still values in list1
        tail.next = list1
        # we save the rest of the values of list1 in tail.next
    else:
        tail.next = list2
        # if list2 still has values that will be saved in tail.next
    return dummy.next
    # you finally return dummy.next because dummy is where the list is saved
```