# Name

242 Valid Anagrams (Needs to be edited)

## Problem

* Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

## Solution

```python
# first solution| Time = O(n), Space = O(1)
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
       return sorted(s) == sorted(t)
       # we sort the strings and we compare the two sorted strings if they are even it will return True. # If not it will return False

# Second Solution | Time = O(n), Space = O(1)
from collections import Counter
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # the counter library stores elements as dictionary keys and the count of the elements as dictionary values
        # Ex: s= car, t = rac. Counter(s) = {"c":1, "a": 1, "r": 1}, Counter(t) = {"r": 1, "a": 1, "c": 1}.
        # because the counts are the same it would return true
```
 