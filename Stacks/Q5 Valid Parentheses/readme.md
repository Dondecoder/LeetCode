# Name

20 Valid Parentheses

## Problem

* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


## Solution Explanation

* To understand and solve this problem you need to understand that stacks are LIFO. Last in first out which means the last thing inputed in a stack will be the first thing taken out. Use a hashtable to store the parenthesis in reverse order. The keys will be the reverse of the parenthesis(ex:),},]) amd the values will be there opposites. While you iterate through the string if the value is not in the hash as in the hash key then append it to the stack and then continue. Stack is an empty list. if c is in Map but not in stack and it does not equal the value that is in the map dictionary then return False. Else pop it off the stack. Else return not stack --> this equals true. 


```python
    class Solution:
        def isValid(self, s: str) -> bool:
            Map = { ")":"(", "]":"[", "}":"{" }
            # you create a hash map with key value pairs that operate similar to a stack the keys are the reverse opposites of the values.
            stack = []
            # empty list 
            
            for c in s:
            # you would iterate through array s
                if c not in Map:
                # if c is not in Map meaning if c is not a key of map
                    stack.append(c)
                    # it will be appended to C
                    continue
                    # it will continue iteration to the next c    
                if not stack or stack[-1] != Map[c]: 
                # if c is in Map but not in stack and it does not equal Map[c] for example Map[")"].
                    return False
                    # return False
                stack.pop()
                # pop it off the stack
                
            return not stack 
            # this happens when you input not to an empty data structue
```