class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def solve(index , size):
            if (index == size):
                return True
            
            if (dp[index] != -1):
                return dp[index]
            left = ''
            for pos in range(index , size):
                
                left += s[pos]
                if (left in words):
                    val = solve(pos+1 , size)
                    if (val):
                        dp[index] = True
                        return dp[index]
            
            dp[index] = False
            return False
        
        words = set(wordDict)
        size = len(s)
        dp = [-1 for _ in range(size)]
        
        ans = solve(0 , size)
        
        return ans