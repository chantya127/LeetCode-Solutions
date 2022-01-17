
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def poss(minutes):
            
            target = minutes*n
            
            curr_dur = 0
            
            for duration in batteries:
                
                if (duration < minutes):
                    curr_dur += duration
                
                else:
                    curr_dur += minutes
                
                if (curr_dur >= target):
                    break
            
            return (curr_dur >= target)
        
        batsum = 0
        for power in batteries:
            batsum += power
        
        low = 0
        high = batsum//n
        
        ans = -1
        
        while(low <= high):
            
            mid =(high-low)//2 + low
            
            if (poss(mid)):
                ans = mid
                low = mid+1
            
            else:
                high = mid-1
        
        return (ans)
        
        
        
        