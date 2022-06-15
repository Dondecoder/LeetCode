# My solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
        # if len(nums) list does not equal len(set(nums)) list 
            return True
            # return True
        else:
            return False
            # return False

# Video Tutorial Solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
        # iterate through the input array
            if n in hashset:
            # if the number is in the set 
                return True
                # return True
            hashset.add(n)
            # else add the 
        return False
        # otherwise return false