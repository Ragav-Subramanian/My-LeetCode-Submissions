class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minimum=[float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minimum.append(min(self.minimum[-1],x))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()