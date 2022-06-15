class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        n = len(words)
        if n == 1:
            return 1
        
        def solve(word):
            
            if word in dp:
                return dp[word]
            
            ans = 1
            
            for i in range(len(word)):
                curr = word[:i] + word[i+1:]
                if curr in seti:
                    ans = max(ans , 1 + solve(curr))
            
            dp[word] = ans
            return ans
        
        seti = set(words)
        res = 1
        dp = {}
        
        for word in words:
            res = max(res , solve(word))
        
        return res