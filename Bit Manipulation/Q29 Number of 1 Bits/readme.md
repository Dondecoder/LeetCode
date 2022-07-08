# Name

191 Number of 1 Bits

## Problem

* Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3. 

## Solution

* For this problem the most optimal solution would be to run the modulo function on the integer and to shift the binary number 1 space to the right. The time complexity and space complexity would be 0(1). Update a count variable with the integer % 2 and it will run as long as n has a value. After that it exits out the loop and returns the count. The way I went about it was to turn the integer into a string and convert the integer to a binary number then turn the binary into a string then iterate through the string and update counter by 1 for each 1 in the string and then return counter. 

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res    

class MyalternativeSolution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        count = 0
        for i in n:
            if i == '1':
                count +=1
        return count
```