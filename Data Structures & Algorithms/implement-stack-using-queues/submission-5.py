from queue import Queue
class MyStack:
    
    def __init__(self):
        self.q1,self.q2 =Queue(), Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        for i in range(self.q1.qsize()-1):
            self.q2.put(self.q1.get())
        for i in range(self.q2.qsize()):
            self.q1.put(self.q2.get())
        return self.q1.get()

    def top(self) -> int:
        for i in range(self.q1.qsize()-1):
            self.q2.put(self.q1.get())
        top = self.q1.get()
        self.q2.put(top)
        for i in range(self.q2.qsize()):
            self.q1.put(self.q2.get())
        return top

    def empty(self) -> bool:
        print(self.q1)
        if(self.q1.qsize() == 0):
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()