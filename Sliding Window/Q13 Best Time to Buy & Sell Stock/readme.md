# Name

121 Best Time to Sell Stock

## Problem

* You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


## Solution Explanation

* To understand and solve this problem it is best to solve this by using two pointers. Use one pointer to be 0 and the other pointer to be 1. Create a variable to equal maxprofit to hold the max numbers. You can use a while loop that will iterate as long as bigger pointer is less than the length of the array. You then check if the value of lower pointer in the index is less than the value of the higher pointer in the index.If it is then calculate the profit by subtracting values from the array that correspond with the lower pointer and the higher pointer than update maxP to equal the max of maxP and the profit. If the lower index value is greater than the higher index value make the lower index equal the higher index and increment the higher index +1. Finally return maxP

```python
# Time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

```