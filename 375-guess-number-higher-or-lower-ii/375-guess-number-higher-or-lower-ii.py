class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        def solve(low , high):
            
            if (low >= high):
                return 0
            
            if (dp[low][high] != -1):
                return dp[low][high]
            
            maxi = float('inf')
            
            for i in range(low , high+1,1):
                
                val = max(solve(low , i-1) , solve(i+1 , high)) + i
                
                maxi = min(maxi , val)
            
            dp[low][high] = (maxi)
            return dp[low][high]
        
        dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]
        return solve(1,n)
        