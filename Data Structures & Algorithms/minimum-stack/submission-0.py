class MinStack:

    def __init__(self):
        self.mini_stack = []

    def push(self, val: int) -> None:
        self.mini_stack.append(val)

    def pop(self) -> None:
        self.mini_stack.pop()

    def top(self) -> int:
        return self.mini_stack[-1]

    def getMin(self) -> int:
        return min(self.mini_stack)
