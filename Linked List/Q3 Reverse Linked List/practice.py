# # Definition for singly-linked list.

# from re import L


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         while head:
#             temp_node = head # 1--> 2 --> 3 --> 4, 5
#             head = head.next # 2 --> 3 --> 4 --> 5 --> none
#             temp_node.next = prev # 1 --> none, 2 -->1--> none, 3 --> 2 --> 1 --> none, 4 -> 3 -> 2 -> 1 -> none, 5 -> 4 -> 3 -> 2 -> 1 -> none
#             prev = temp_node # 1 , 2, 3, 4, 5
#         return prev            

# test = Solution()
# ll = ListNode(1,2)
# ll
# test.reverseList({})

class Solution:
    def isValid(self, s: str) -> bool:
        value_checker = {"}":"{", "]": "[", ")":"("}
        stack = []
        
        if len(s) <= 1:
            return False
        
        for i in s:
            if i not in value_checker:
                stack.append(i)
                continue
            elif value_checker[i] in stack:
                stack.remove(value_checker[i])
                
        
        if len(stack) != 0:
            return False
        else:
            return True


solve = Solution()
solve.isValid("([)]")