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


# Working on optimization

class MinStack3:
    def __init__(self):
        self.stack = list()
        self.minstack = list()
    
    def push(self, val:int):
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1] > val:
                self.minstack.append(val)
            else:
                pass
        else:
            self.minstack.append(val)
    
    def pop(self):
        self.stack.pop()
        if len(self.minstack) > 1:
            self.minstack.pop()
        else:
            pass
    
    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.minstack[-1]


