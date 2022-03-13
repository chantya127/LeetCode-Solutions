class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dd = {'}':'{' , ')':'(' , ']':'['}
        for i in s:
            if i in ['{' , '[' , '(']:
                stack.append(i)
            elif  stack and stack[-1] == dd[i]:
                stack.pop()
            else:
                return False
            
        return stack == []    
            
        