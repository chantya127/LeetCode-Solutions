
#  2

# digits = [1,2,3] , k= 4

# [1,3] , k = k - idx*(size-1) =>3 - 1*2 = 1

# [1] , k = 1 - 1*1 = 0
 

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def solve(ans , size , k , digits):
            
            if (len(digits) == 1):
                ans[0] += str(digits[0])
                return
            
            idx = k // fact[size-1]
            ans[0] += str(digits[idx])
            
            digits.pop(idx)
            
            k -= idx*(fact[size-1])
            
            solve(ans , size-1 , k , digits)
            
            
        
        if (n == 1):
            return str(n)
        
        ans = [""]
        fact = [0]*(n+1)
        fact[1] = 1
        fact[2] = 2
        
        for i in range(3,n+1):
            fact[i] = fact[i-1]*i
        
        digits =[i+1 for i in range(n)]
        
        solve(ans , n , k-1 , digits)
        return ans[0]