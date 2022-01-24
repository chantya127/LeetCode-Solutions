
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def poss(speed):
            
            time = 0
            
            for ban in piles:
                
                time += math.ceil(ban/speed)
                
            return (time <= h)
        
        size = len(piles)
        
        maxi = max(piles)
        
        low = 1
        high = maxi
        ans = -1
        
        while(low <= high):
            
            mid = (high - low)//2 + low
            
            val = poss(mid)
            
            if (val):
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)