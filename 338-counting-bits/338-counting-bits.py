class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count_bits(num):
            
            count = 0
            while(num):
                
                if(num&1):
                    count +=1
                
                num >>=1
            
            return (count)
        
        ans = []
        for num in range(n+1):
            bits = count_bits(num)
            ans.append(bits)
        
        return ans