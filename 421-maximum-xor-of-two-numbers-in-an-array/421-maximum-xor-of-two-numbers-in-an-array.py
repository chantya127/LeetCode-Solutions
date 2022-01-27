class node:
    
    def __init__(self):
        self.child = {}
        self.num = -1
        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        def push(root , num):
            
            bits = bin(num)[2:].zfill(32)
            temp = root
            
            for b in bits:
                
                if (b not in temp.child):
                    temp.child[b] = node()
                
                temp = temp.child[b]
            
            temp.num = num
        
        def query(root ,num):
            
            bits = bin(num)[2:].zfill(32)
            temp = root
            
            for b in bits:
                
                if (b == '0'):
                    rev = '1'
                
                else:
                    rev = '0'
                
                if (rev in temp.child):
                    temp = temp.child[rev]
                
                else:                
                    temp = temp.child[b]
            
            return (num^ temp.num)
        
        root = node()
        size = len(nums)
        
        ans = 0
        
        push(root , nums[0])
        
        for idx in range(1 , size,1):
            
            curr = nums[idx]
            
            val = query(root, curr)
            
            ans = max(ans,val)
            
            push(root , nums[idx])
        
        return (ans)