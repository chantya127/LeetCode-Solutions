class Bitset:

    def __init__(self, size: int):
        self.arr= [0]*(size)
        self.change = 0
        
        self.total = 0
        self.size = size
        

    def fix(self, idx: int) -> None:
        if (self.change + self.arr[idx])%2==0:
            self.arr[idx] += 1
            self.total +=1
        

    def unfix(self, idx: int) -> None:
        if (self.change + self.arr[idx])%2 ==1:
            self.arr[idx] -=1
            self.total -=1

    def flip(self) -> None:
        
        self.total = self.size - self.total
        self.change +=1
        

    def all(self) -> bool:
        return self.total == self.size
        

    def one(self) -> bool:
        return self.total >0
        

    def count(self) -> int:
        
        return self.total
        

    def toString(self) -> str:
        
        ans = ""
        for idx in range(self.size):
            
            if(self.change + self.arr[idx])%2 ==0:
                ans += "0"
            
            else:
                ans += "1"
                
        return (ans)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()