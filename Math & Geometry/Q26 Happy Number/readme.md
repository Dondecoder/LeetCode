# Name

202 Happy Number

## Problem

* Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


## Solution Explanation

* In solving this problem we take advantage of the set data structure. We check to see if n is already in the set if not then we add it. Then we use a helper function to extract or split the numbers so we can square then. The helper function calculates the addition of the split numbers squared. It uses the modulo funciton to extract one number and // to extract the other. It adds it to the output and returns the output. If the number is equal to 1 then we exit and return True. If not we return False. 

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = self.splitnum(n)
            
            if n == 1:
                return True
        return False
    
    def splitnum(self,n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output

```