from collections import deque
class MinStack:

    def __init__(self):
        self.arr = []
        self.global_min = float('inf')
        
    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr.append((val, val))
        else:
            self.arr.append((val, min(val, self.arr[-1][1])))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]
        
    def getMin(self) -> int:
        return self.arr[-1][1]
        
