class MinStack:

    def __init__(self):
        self.min_val = []
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.min_val:
            self.min_val.append(min(val, self.min_val[-1]))
        else:
            self.min_val.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.min_val.pop()
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
