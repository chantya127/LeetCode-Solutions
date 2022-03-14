class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #print(path.split('/'))
        
        from collections import deque
        stack = deque()
        for p in path.split('/'):
            
            if len(p) == 0 or p == '.':
                continue
            
            elif p == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)
            