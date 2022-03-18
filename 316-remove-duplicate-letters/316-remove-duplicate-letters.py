from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        
        count = defaultdict(int)
        instack  = defaultdict(int)
        stack = []
        
        for ch in s:
            count[ch] +=1
        
        for ch in s:
            
            while(stack and stack[-1] > ch):
                
                prev = stack[-1]
                #print(prev)
                if (prev > ch and count[prev] > 0 and not instack[ch]):
                    
                    stack.pop()
                    instack[prev] = 0
                
                else:
                    break
                    
            if (not instack[ch]):
                stack.append(ch)
                instack[ch] = 1
                
            count[ch] -=1
            
        
        return ("".join(stack))