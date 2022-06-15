# Name

206 Reverse Linked List

## Problem

* Given the head of a singly linked list, reverse the list, and return the reversed list.


## Solution Explanation

The trick to understanding this problem is rather than iterating through the whole linked list until you hit the end or none value, work on changing the pointers in the list to point in the opposite direction. Break up the large problems into subproblems and focus on having each pointer point in the opposite direction. Save the value of the head node and create a pointer = None. Iterate through the list using a while loop as long as their's a head node and update prev as you iterate and make head = head.next. Continue until your LL hits a none value and then return prev. 

For example:
    ```5 --> 4 --> 3 --> 2```
    In this example focus on making the pointers point in the opposite direction so make 4 point to 5, 3 point to 4 and 2 point to 3. This in turn will reverse the linked list. 


```python
# Time = O(n) | Space = O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        # you set a pointer that equals None
        while head:
        # while there is a head node
            temp_node = head
            # you save the value of the head node in a variable called temp_node
            head = head.next
            # you set the head node to equal the next node 
            temp_node.next = prev
            # you set the pointer of the previous head node to equal prev
            prev = temp_node
            # now prev = temp_node that was saved
        return prev            
```