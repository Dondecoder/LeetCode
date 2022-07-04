class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])


cost_stair = Solution()
cost_stair.minCostClimbingStairs(
[1,100,1,1,1,100,1,1,100,1])