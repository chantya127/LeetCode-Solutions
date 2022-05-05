class MyStack:

    def __init__(self):
        
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        
        
        while(self.q1):
            
            ele = self.q1.pop(0)
            
            self.q2.append(ele)
        
        
        self.q1.append(x)
        
        while(self.q2):
            
            ele = self.q2.pop(0)
            
            self.q1.append(ele)
        

    def pop(self) -> int:
        
        return self.q1.pop(0)
        

    def top(self) -> int:
        
        return self.q1[0]
        

    def empty(self) -> bool:
        
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


[1,2,3]

q2 = [3,2,1]

q1 = [4,3,2,1]


3
2
1