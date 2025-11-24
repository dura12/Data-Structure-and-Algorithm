class MinStack:

    def __init__(self):
        self.stack = [[0 , float("inf")]]

    def push(self, val: int) -> None:
        self.stack.append([val , min(self.stack[-1][1] , val)])
    def pop(self) -> None:
        if len(self.stack) < 2:
            raise Exception("empty list")
        self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) < 2:
            raise Exception("empty list")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) < 2:
            raise Exception("empty list")
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()