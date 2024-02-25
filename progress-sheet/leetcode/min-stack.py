class MinStack:

    def __init__(self):
        self.stk = []
        self.mn = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mn or self.mn[-1]>val:
            self.mn.append(val)
        else:
            self.mn.append(self.mn[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()