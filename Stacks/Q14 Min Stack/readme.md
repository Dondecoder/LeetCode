# Name

155 Min Stack

## Problem

* Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


## Solution Explanation

* To understand and solve this problem you need to pretty much implement a min stack. A min stack pretty much is a regular stack except the min number in the stack is on the top. This one is tricky because you have to retrieve the min number in the stack in constant time which is O(1) time. The min function uses O(n) time because it's iterating over the stack. So the big takeaway with this is create another list called min stack in the init function of the class. Append the min value and compare the current value being appended and the value at index[-1] of the minstack. If the minStack is empty it will just append the value to the min stack. Otherwise it will compare both values. For the function which says return min number you just return the number at index [-1] in the min stack.  

```python
# Solution 1
# Time: O(n)| Space: O(n)
class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        return self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)

# Solution 2
# Time: O(1) | Space: O(n)

class MinStack2:
    def __init__(self):
        self.stack = list()
        self.minstack = list()
    
    def push(self, val:int):
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1] if self.minstack else val))
    
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    
    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.minstack[-1]

```

