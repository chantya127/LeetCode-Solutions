class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def solve(limit):
            
            summe = weights[0]
            count = 1
            
            for idx in range(1,size):
                
                curr = weights[idx]
                if (curr > limit):
                    return False
                
                summe += curr
                if (summe > limit):
                    summe = curr
                    count +=1
                
                if (count > days):
                    break
            
            return (count <= days)
        
        size = len(weights)
        
        low = max(weights)
        
        high = sum(weights)+1
        
        ans =-1
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            # print(mid, low,high)
            if (solve(mid)):
                
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)