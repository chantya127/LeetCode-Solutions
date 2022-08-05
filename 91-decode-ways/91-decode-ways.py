class Solution:
    def numDecodings(self, s: str) -> int:
        
        def solve(pos , size,dp):
        
            if (pos >=  size):
                return 1
            
            if (dp[pos] != 0):
                return dp[pos]
            
            count = 0
            
            if (s[pos] > '0'):
                count = solve(pos+1 , size,dp)
            
            if (pos+1 < size) and (s[pos]=='1' or (s[pos] == '2' and s[pos+1] < '7')):
                count += solve(pos+2 , size,dp)
            
            dp[pos] = count
            return (count)
        
        
        size = len(s)
        dp= [0 for _ in range(size)]
        ans = solve(0 , size ,dp)
        
        return ans