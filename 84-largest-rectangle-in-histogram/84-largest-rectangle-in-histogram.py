class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = 9999
        n = len(heights)
        llb = [maxi]*(n)
        rlb = [maxi]*(n)
        
        
        llb[0] = -1
        stack = [0]
        for i in range(1,n):
            while len(stack) and (heights[stack[-1]] >= heights[i]):
                stack.pop()
            if len(stack) ==0 :
                llb[i] = -1
            else:
                llb[i] = stack[-1]
            stack.append(i)   
        
        stack = [n-1]
        rlb[n-1] = n
        for i in range(n-2,-1,-1):
            while len(stack) and heights[stack[-1]] >= heights[i]:
                stack.pop()
                
            if len(stack) ==0:
                rlb[i] = n
            else:
                rlb[i] = stack[-1]
            stack.append(i)    
            
        
        area = 0
        for i in range(n):
            area = max(area , heights[i]* (rlb[i] - llb[i]-1))
        return area    