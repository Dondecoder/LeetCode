from collections import Counter
from time import time
# My solution is slow but works
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        for i in t:
            if s.count(i) != t.count(i):
                return False
        return True

        

# second solution
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

# third solution
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
       return sorted(s) == sorted(t)


# forth solution
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)



print(Solution1().isAnagram('anagram', 'nagaram'))
