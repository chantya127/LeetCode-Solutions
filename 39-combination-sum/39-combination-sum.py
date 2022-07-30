class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def solve(idx , size , target , curr):
            
            if (target == 0):
                ans.append(curr)
                return
            
            if (idx == size):
                return 
            
            if (candidates[idx] <= target):
                solve(idx , size , target - candidates[idx] , curr + [candidates[idx]])
            
            solve(idx+1 , size,target , curr)
        
        ans = []
        
        solve(0,len(candidates) , target , [])
        
        return ans