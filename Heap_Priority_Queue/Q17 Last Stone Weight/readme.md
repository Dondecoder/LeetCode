# Name

1046 Last Stone Weight

## Problem

* You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

## Solution

* To understand this problem you need to know when to use heaps. Using pythons heapq module we can build a min heap which sorts the first number in the list and continues sorting as the list is updated. Since python heaqq can only do min heaps we get around that by converting the numbers into negatives when recreating the stones array. Then we use the heapq.heapify to convert it into a heap. We use a while loop that will run as long as the length of the stones array is greater than 1. We save the two minimum values in the variable called first and second by popping the minimum values off the array. If the second value is greater than the first we push to the heap the subtraction of the first - second then we continue running the while loop as long as the len(stones) is > 1. We keep on doing that until the len(stones) array is 1. We break the loop and then append 0 to the array (This is for the edge case if the array is empty). Finally we return abs(stones[0]).

```python
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
```