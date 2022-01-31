class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        prev, summe = 0,float('-inf')
        
        for curr in nums:
            
            if (prev >=0):
                prev += curr
            
            else:
                prev = curr
            
            if(prev > summe):
                summe = prev
        
        return (summe)