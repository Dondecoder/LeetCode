class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)
        
        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False
            
    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output


class Solution2:
    def isHappy(self,n:int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.SumOfSquares(n)

            if n == 1:
                return True
        return False

    def SumOfSquares(n):
        output = 0
        while n:
            output += (n%10) ** 2
            n = n // 10
        return output 


Happy_num = Solution()
Happy_num.isHappy(19)