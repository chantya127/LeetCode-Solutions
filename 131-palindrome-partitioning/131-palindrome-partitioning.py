class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def solve(pos , res):
            
            if (pos >= size):
                
                ans.append(res[:])
                return
            
            
            
            for idx in range(pos , size,1):
                
                left = s[pos : idx+1]
                
                if (left == left[::-1]):
                    solve(idx+1 , res + [left])
            
        
        size = len(s)
        
        ans = []
        
        solve(0 , [])
        return ans
        
        # a -> a -> b