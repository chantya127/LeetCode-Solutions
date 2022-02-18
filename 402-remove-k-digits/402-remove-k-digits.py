class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if (k >= len(num)):
            return "0"
            
        ans = "0"
        
        stack = []
        
        for curr in num:
            
            while(stack and k and stack[-1] > curr):
                k-=1
                stack.pop()
            
            stack.append(curr)
        
        while(k and stack):
            stack.pop()
            k-=1
        
        for i in range(len(stack)):
            if (stack[i] == "0" and i != len(stack)-1):
                stack[i] = ""
            
            else:
                break
                
        
        return "".join(stack)