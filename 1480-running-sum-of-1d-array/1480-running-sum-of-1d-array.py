class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        summe = nums[0]
        for idx in range(1,len(nums)):
            nums[idx] += summe
            summe = nums[idx]
        
        return nums