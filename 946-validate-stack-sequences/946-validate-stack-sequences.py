class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        
        size = len(pushed)
        p1,p2 = 0,0
        
        while(p1 < size and p2 < size):
            
            pushed_val = pushed[p1]
            stack.append(pushed_val)
            p1 +=1
            
            while(p2 < size and stack and stack[-1] == popped[p2]):
                stack.pop()
                p2 +=1
                
                
        while(p2 < size and stack and stack[-1] == popped[p2]):
            stack.pop()
            p2 +=1
            
        return (len(stack) == 0 and p1 == size and p2 == size)
        