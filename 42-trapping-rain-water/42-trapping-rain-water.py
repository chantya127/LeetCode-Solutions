class Solution:
    def trap(self, height: List[int]) -> int:
        
        size = len(height)
        
        
        left = [0]*(size)
        right = [0]*(size)
        
        left[0] , right[-1] = height[0] , height[-1]
        
        for idx in range(1,size):
            
            left[idx] = max(left[idx-1] ,height[idx])
        
        for idx in range(size-2,-1,-1):
            right[idx] = max(right[idx+1] , height[idx])
        
        total_capacity = 0
        # print(left)
        # print(right)
        # print(height)
        
        for idx in range(1,size-1,1):
            
            min_height = min(left[idx] , right[idx])
            curr_capacity = min_height - height[idx]
            
            
            total_capacity += curr_capacity
        
        return (total_capacity)