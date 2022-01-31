class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        for idx in range(size):
            
            curr = (nums[idx])%size
            nums[curr] += size
        
        for idx in range(1,size):
            
            if (nums[idx]//size)>1:
                return (idx)
        
        