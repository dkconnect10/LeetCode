class MyQueue:

    def __init__(self):
        self.temp = []

    def push(self, x: int) -> None:
        self.temp.insert(0,x)

    def pop(self) -> int:
        return self.temp.pop(-1)

    def peek(self) -> int:
        return self.temp[-1]

    def empty(self) -> bool:
        return len(self.temp)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()