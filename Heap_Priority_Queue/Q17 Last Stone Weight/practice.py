# Incorrect Solution
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        l = 0
        r = 1
        stones.sort()
        while r <= len(stones) - 1:
            if len(stones) == 1:
                return stones[0]
            elif stones[l] == stones[r]:
                stones.remove(stones[l])
                stones.remove(stones[r])
            elif stones[l] != stones[r]:
                stones[r] = stones[r] - stones[l]
                stones.remove(stones[l])
            l += 1
            r += 1
        if len(stones) < 1:
            return 0 
        return stones[0]

# Correct Solution 
import heapq

class Solution2:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])



stones_weight = Solution()
stones_weight.lastStoneWeight([2,2])