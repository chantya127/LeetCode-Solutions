from collections import defaultdict

class FreqStack:

    def __init__(self):
        
        self.num_freq = defaultdict(int)
        
        self.freq_ele = defaultdict(list)
        self.max_freq = 0
        
        
    def push(self, val: int) -> None:
                
        self.num_freq[val] +=1
        freq =  self.num_freq[val]
        #print(self.num_freq[val])
        
        if (self.num_freq[val] > self.max_freq):
            self.max_freq = self.num_freq[val]
            
        self.freq_ele[freq].append(val)
        
        

    def pop(self) -> int:
        
        
        val = self.freq_ele[self.max_freq].pop()
        self.num_freq[val] -=1
        
        if len(self.freq_ele[self.max_freq]) == 0:
            self.max_freq -=1
        
        return (val)
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()