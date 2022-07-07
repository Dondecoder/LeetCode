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

Add_one = Solution2()
Add_one.plusOne([9,8,9])