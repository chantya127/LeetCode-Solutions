class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        left =[1 for _ in range(size)]
        left_prod = nums[0]
        
        for idx in range(1 , size,1):
            left[idx] *= left_prod
            
            left_prod *= nums[idx] 
        
        # print(left)
        right = nums[-1]
        
        for idx in range(size-2,0,-1):
            
            
            # print(nums[idx] , right ,left[idx])
            left[idx]*=right
            right = right*nums[idx]
            
        
        left[0] = right
        
        return left
            