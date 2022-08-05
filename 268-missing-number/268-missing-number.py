class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = 0
        for idx in range(len(nums)):
            ans = ans ^idx ^nums[idx]
        
        return (ans ^ len(nums) )