class MinStack:
    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        if not self.values:
            current_min = val
        else:
            current_min = min(val, self.values[-1][1])

        self.values.append([val, current_min])

    def pop(self) -> None:
        self.values.pop()
        
    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]
