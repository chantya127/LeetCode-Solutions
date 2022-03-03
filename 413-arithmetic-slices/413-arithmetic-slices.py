class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n= len(nums)
        if (n<3):
            return 0
        
        val = 0
        prev = 0
        for i in range(2,n):
            
            d1 ,d2 = nums[i]- nums[i-1] ,nums[i-1] - nums[i-2]
            
            if (d1 == d2):
                
                prev = prev+1
                val +=prev
            
            else:
                prev = 0
        
        return (val)
        
        
        