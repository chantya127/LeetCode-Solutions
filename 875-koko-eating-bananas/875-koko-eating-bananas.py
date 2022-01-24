from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def pos(speed):
            
            time = 0
            
            for ban in piles:
                
                time+= ceil(ban/speed)
            
            return (time <= h)
        
        low = 1
        high = max(piles)
        ans = -1
        
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            
            if (pos(mid)):
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)