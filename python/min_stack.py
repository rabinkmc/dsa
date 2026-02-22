class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
            return
        self.st.append((val, min(val,self.st[-1][1])))
        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]
        

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
obj.top()
obj.getMin()
