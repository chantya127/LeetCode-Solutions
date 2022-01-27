class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        size = len(colors)
        
        count = {"A" :0 , "B" : 0}
        ptr = 0
        
        while(ptr <size):
            
            st  = ptr
            curr = colors[ptr]
            while(ptr < size and colors[ptr] == curr):
                ptr +=1
            
            length = ptr - st
            if (length > 2):
                
                count[curr] += length-2
            
        
        return (count["A"] > count["B"])