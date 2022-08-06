class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def solve(s1,s2):
            
            if (s1 == 0 or s2 == 0):
                return 0
            
            if (text1[s1-1] == text2[s2-1]):
                return solve(s1-1,s2-1) +1
            
            else:
                return max(solve(s1-1,s2) , solve(s1,s2-1))
        
        s1,s2 = len(text1) , len(text2)
        
        ans = solve(s1,s2)
        return ans