# Name

66 Plus One

## Problem

* You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Solution Explanation

* To solve this problem we need to first consider edge cases such as the number 9 and if the digits array has multiple 9's. To combat that edge case you would need to convert each 9 into 0's and add a 1 to the list. Use a while loop that will run given a variable that has a value such as 1 and create an i variable that will be used to traverse the array. As long as i is less than length of array and if array[i] == 9 then array[i] = 0. If not then we increase array[i] + 1 and decrement the variable that equals one so the while loop can be broken. Then we return the digit array in reverse order. Alternatively to avoid having to reverse the array we can assign i to equal len(array) - 1 and as long i >= 0 we update any 9's to 0 and we decrement i. while i >= 0 if the array[i] is not 9 we just increase it by 1 and return the array. Finally after breaking the while loop if i < 0. We just add [1] + array and return it. 

```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        one = 1
        i = 0
        digits = digits[::-1]
        
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]

class Solution2:
    def plusOne(self, digits:list[int]):
        i = len(digits)-1
        while i >= 0:
            if (digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1    
        return [1] + digits

Add_one = Solution()
Add_one.plusOne([9,8,9])

```