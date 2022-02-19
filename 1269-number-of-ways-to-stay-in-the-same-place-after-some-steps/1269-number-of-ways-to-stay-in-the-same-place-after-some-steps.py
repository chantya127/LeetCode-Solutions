mod = (10**9) +7

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        arrLen = min(arrLen, steps + 1)
        dp = [[0 for _ in range(arrLen)] for _ in range(steps+1)]
        
        dp[0][0] = 1
        
        for step in range(1,steps+1):
            
            for idx in range(arrLen):
                
                val = 0
                
                if (dp[step-1][idx] > 0):
                    
                    val = dp[step-1][idx]
                
                if (idx>0 and dp[step-1][idx-1] > 0):
                    val = (val + dp[step-1][idx-1])%mod
                
                if (idx +1 < arrLen and dp[step-1][idx+1] > 0):
                    val = (val + dp[step-1][idx+1])%mod
            
                dp[step][idx] = val
            
        return (dp[steps][0])