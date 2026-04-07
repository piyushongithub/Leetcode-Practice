class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.minstack[-1],val) if self.minstack else val
        self.minstack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

        
