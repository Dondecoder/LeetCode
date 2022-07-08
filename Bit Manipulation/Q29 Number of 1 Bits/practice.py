import time

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res

class Solution2:
    def hammingWeight(self, n:int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

class MyalternativeSolution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        count = 0
        for i in n:
            if i == '1':
                count +=1
        return count

Bit_1 = Solution2()
Bit_1.hammingWeight(n=0b00000000000000000000000000001011)
# print(38639 % 2)