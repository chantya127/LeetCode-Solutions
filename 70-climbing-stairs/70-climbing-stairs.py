class Solution:
    def climbStairs(self, n: int) -> int:
        
        if (n<4):
            return n
        
        a,b = 1,2
        while(n-2):
            c = a+b
            a = b
            b = c
            n-=1
        
        return c