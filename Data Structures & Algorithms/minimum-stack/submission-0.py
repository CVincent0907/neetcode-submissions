class MinStack:

    def __init__(self):
        self.ls = []
        

    def push(self, val: int) -> None:
        self.ls.append(val)

    def pop(self) -> None:
        self.ls.pop()

    def top(self) -> int:
        return self.ls[-1]   

    def getMin(self) -> int:
        minimum = self.ls[0]
        for num in self.ls:
            if num < minimum:
                minimum = num
        return minimum
