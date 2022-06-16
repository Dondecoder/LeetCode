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