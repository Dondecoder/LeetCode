# Name

20 Kth Largest Element in a Stream

## Problem

* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


## Solution Explanation

* To understand and solve this problem you need to understand what are heaps and what are the funtionality of them. Heaps are a data structure that are capable of giving you the smallest or largest element by some criteria in constant time (O(1)). It can add elements and remove the smallest(min-heap) or largest (max-heap) in O(log(n)). It can perform insertions and removals while always maintaining the first property. Heaps work with arrays so you can turn an array into a heap by passing it through a heap function. If its a min heap it will sort and the heappop will pop the smallest element in the heap. The reason the length of the heap needs to be equal to k is because you are suppose to return the kth largest element. If the heap is size k then the first element in the heap will be the kth largest element. 


```python
import heapq

class KthLargest:
     
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.miniheap = nums
        # we could've called this anything to equal to nums
        heapq.heapify(self.miniheap)
        # we use this function to turn the list into a heap because it is efficient for faster insertion and it stores elements in sorted order and heapq can add elements and remove smallest elements using their heappop function
        
        while len(self.miniheap) > self.k:
        # while the length of the miniheap is greater than k
            heapq.heappop(self.miniheap)
            # it will pop the smallest element off the miniheap
        

    def add(self, val: int) -> int:
        heapq.heappush(self.miniheap, val)
        # this is for the add function and it is used to push or add a value to the mini heap
        if len(self.miniheap) > self.k:
        # similar to above if the len of the miniheap is greater than k 
            heapq.heappop(self.miniheap)
            # it will pop the smallest value of the miniheap
        return self.miniheap[0]
        # this will return the Kth smallest value because it will always be at index 0 because the heap automatically sorts the numbers in ascending order

```