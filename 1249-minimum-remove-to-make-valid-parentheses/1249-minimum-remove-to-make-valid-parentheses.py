class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        ss = list(s)
        for idx in range(len(s)):
            
            ch = ss[idx]
            if (ch == '('):
                stack.append(idx)
            
            elif(ch == ')'):
                if (stack):
                    stack.pop()
                
                else:
                    ss[idx] = ''
        
        for idx in stack:
            ss[idx] = ''
        
        # print(ss)
        return ''.join(ss)