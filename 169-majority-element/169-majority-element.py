class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        count = 1
        majority = nums[0]
        
        for idx in range(1,size,1):
            
            curr = nums[idx]
            if (curr == majority):
                
                count +=1
            
            else:
                count -=1
            
            if (count == 0):
                majority = curr
                count = 1
        
        return (majority)