
# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     for i in range(strs):
#         for j in range(1,strs):
#             if (strs[i][0,2] == strs [j][0,2]):
#                 print(strs[i][0,2])

# longestCommonPrefix(["flower","floor","flee"])

    
    # Write your logic here
# def is_leap(year):
#     leap = False
    
#     # Write your logic here
   
#     if (year % 4 == 0) and (year % 100 > 0) or (year % 400 == 0):
#         return True
   
#     else:
#         return leap

# year= 2000
# print(is_leap(year))
# # print(year % 400)


# class Solution:
#     def runningSum(nums: list[int]) -> list[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
#         print(nums)
              


# Solution.runningSum([1,2,3,4,5])


# Python Program to
# show range() basics
 
# printing a number
for i in range(10):
    print(i, end=" ")
print()
 
# using range for iteration
l = [10, 20, 30, 40]
for i in range(1,len(l)):
    print(l[i], end=" ")
print()
 
# performing sum of natural
# number
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)