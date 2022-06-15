# Name

125 Valid Palindrome

## Problem

* A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


## Solution Explanation

* To understand and solve this problem you need to first make sure that the values being compared are lowercase and to remove non alphanumeric characters from the string. Ideally in Solution1 and Solution3 we create pointers to compare the beginining of a string to the end of the string and if the values are equal all through the iteration of the string then it is a valid palindrome. If any value is different then it is not a valid palindrome. There are many ways to acheive this you can use regular expression, python built in string functions, or create a helper function that will check if each value in the string is alphanumeric. 

```python
# Solution 1
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        start,end = 0, len(new_string) - 1
        while start <= end:
            if new_string[start].lower() == new_string[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True


# Solution 2
class Solution2:
    def isPalindrome(self, s: str):
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# Solution 3
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]): 
                l += 1
            while l < r and not self.alphanum(s[r]): 
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1
            r -= 1
        return True
    
    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

```