# Name

746 Min Cost Climbing Stairs

## Problem

* You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

## Solution Explanation

* To understand and solve this problem you need to understand how to implement dynamic programming for repeated funcitons. With this problem we need to find the min cost to reach the top of the stairs. The top of the stairs is not the last value in the cost array it is the empty value after it. To solve we update the cost array by appending a 0 to it which will represent the last "cost" value in this array. The we will reverse iterate through this array the reason we do this is to make sure that no matter what we will always be able to compare i + 1 and i +2 because we first append a 0 to the end of the array which will be the top. Then we continue iterating through the array backwords and update values on the array based on min of cost[i] and cost[i+1] we add those values to the array until we reach the front of the array then we return the min value of the 1st and 2nd element in the array. 


```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])
```