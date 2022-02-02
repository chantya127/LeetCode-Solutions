class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(num , power):
            
            if (power <=0):
                return 1
            
            if(power == 1):
                return (num)
            
            if(power in dp):
                return (dp[power])
            
            val = solve(num,power//2)
            val = val*val
            
            if (power%2 ==1):
                
                val = (val*num)
            
            dp[power] = val
            return (dp[power])
                
        
        sign = 1
        rev = 0
        
        if(n<0):
            rev = 1
        
        if(x<0 and n%2 ==1):
            sign = -1
        
        x = abs(x)
        n = abs(n)
        dp = {}
        res = solve(x,n)
        res = res*sign
        
        if(rev == 1):
            res = (1 / res)
        
        return (res)