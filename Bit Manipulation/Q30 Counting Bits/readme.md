# Name

338 Counting Bits

## Problem

* Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## Solution

* To understand this problem you have to think dynamic programming. This is typically used in process that will repeat itself or repeated action. Create an array that is the size of n + 1. Then create a variable that will start with 1. Use a for loop that will iterate as long as we start from range 1 to n +1. You are iterating until you find a number that is a multiple of 2 then if the variable * 2 = i then update offset to equal i. Then update the i value in the ans array to be 1 + the value of ans[i - offset]. Finally return ans.

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
        return ans     
```