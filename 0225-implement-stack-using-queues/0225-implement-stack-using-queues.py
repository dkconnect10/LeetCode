class MyStack:

    def __init__(self):
        self.temp=[]

    def push(self, x: int) -> None:
        self.temp.insert(0,x)

    def pop(self) -> int:
        return self.temp.pop(0)

    def top(self) -> int:
        return self.temp[0]

    def empty(self) -> bool:
        return len(self.temp)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()