class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        
        def solve(idx , summe , res):
            
                
            if (summe == target):
                ans.append(res[:])
                return
            
            if (idx == size or summe > target):
                return
            
            #print(idx, summe , res)
            for pos in range(idx , size,1):
                
                curr = cand[pos]
                
                if (pos>idx and cand[pos] == cand[pos-1]):
                    continue
                
                if(summe + curr <= target):
                    solve(pos+1 , summe +curr , res+[curr])
                
                else:
                    break
                    
                
        
        cand.sort()
        size = len(cand)
        
        #print(cand)
        ans = []
        solve(0,0,[])
        
        return ans