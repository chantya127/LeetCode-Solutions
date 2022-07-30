class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        size = len(nums)
        
        max_reach = nums[0]
        
        for idx in range(size-1):
            
            if (idx > max_reach):
                break
            curr_reach = nums[idx] +idx
            
            max_reach = max(max_reach , curr_reach)
            
            if (max_reach >= size-1):
                break
            
        
        
        return max_reach >= size-1