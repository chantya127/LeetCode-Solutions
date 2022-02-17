class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        
        def solve(idx , summe , curr):
            
            if idx == size :
                if (summe == target):
                    ans.append(curr[:])
                    
                
                return
            
            if (summe + cand[idx] <= target):
                solve(idx , summe+cand[idx] , curr + [cand[idx]])
            
            solve(idx+1 ,  summe , curr)
            
                
        size = len(cand)
        
        ans = []
        
        solve(0 , 0,[])
        
        return ans