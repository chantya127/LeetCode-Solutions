from collections import defaultdict

class Solution:
    def maximumUniqueSubarray(self, arr: List[int]) -> int:
        
        vis = set()
        
        i ,j= 0 ,0

        n = len(arr)
        ans , summe = 0 ,0
        
        while (i<n and j<n):
            
            val = arr[i]
            if val not in vis:
                vis.add(val)
                summe+=val
                ans = max(ans , summe)
                i+=1
            
            else:
                res = arr[j]
                vis.remove(res)
                summe -=res
                j+=1

        return ans        
                
            
            
        
        