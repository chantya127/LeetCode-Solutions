class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        # 1101 -> 1011
        
        temp = 0
        
        for _ in range(32):
            
            temp  = temp << 1
            temp = temp | n&1
            
            n = n>>1
                    
        return (temp)