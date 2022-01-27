#User function Template for python3
mod = (10**9+ 7)
class Solution:
    #Complete this function
    def power(self,n,r):
        #Your code here
        
        def solve(num ,power,dp):
            
            if (power <=0):
                return 1
            
            if (power == 1):
                return (num)
            
            if (power in dp):
                return (dp[power])
                
            val = solve(num , power//2 , dp)
            val = (val*val)%mod
            
            if (power%2 == 1):
                
                val = (val *num)%mod
            
            dp[power] = val
            return (dp[power])
        
        dp = {}
        
        ans = solve(n,r,dp)
        
        return (ans)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends