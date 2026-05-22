class MinStack:

    def __init__(self):
        self.ls = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.ls:
            self.ls.append(val)
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
            self.ls.append(val)

    def pop(self) -> None:
        self.ls.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.ls[-1]   

    def getMin(self) -> int:
        return self.minStack[-1]
