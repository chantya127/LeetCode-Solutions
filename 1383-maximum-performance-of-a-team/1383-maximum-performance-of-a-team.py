from heapq import heappush as push, heappop as pop
mod = 10**9+7

class Solution:
    def maxPerformance(self, n: int, speed: List[int], eff: List[int], k: int) -> int:
        
        poss = [[speed[idx] ,eff[idx]] for idx in range(n)]
        poss.sort(key = lambda it :it[1] , reverse = True)
        
        ans = 0
        heap = []
        summe = 0
        
        for idx in range(n):
            
            sp , e = poss[idx][0],poss[idx][1]
            
            if (len(heap) == k):
                summe -= pop(heap)
            
            summe += sp
            push(heap , sp)
            curr_per = e * summe
            ans = max(ans , curr_per)
            
            
        return (ans)%mod
                    
                
            
            
            