class Solution:
    def rob(self, nums: List[int]) -> int:

        
        inc,exc = nums[0],0
        
        for num in nums[1:]:
            
            new_inc = num + exc
            new_exc = max(inc , exc)
            
            inc = new_inc 
            exc = new_exc
        
        return max(inc,  exc)
            
        
        
     #     1 ,2 ,3 ,1
     # inc 1  2  4  3
     # exc 0  1  2  4