class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        op,cl = 0,0
        ans= 0
        for ch in s:
            if (ch == "("):
                op+=1
            
            else:
                cl +=1
            
            if (op == cl):
                ans = max(ans , cl)
        
        
            if (cl > op):
                op =0
                cl =0
        
        op,cl = 0,0
        for ch in s[::-1]:
            if (ch == "("):
                op+=1
            
            else:
                cl +=1
            
            if (op == cl):
                ans = max(ans , cl)
        
        
            if (cl < op):
                op =0
                cl =0    
            
        return (ans*2)