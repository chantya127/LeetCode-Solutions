class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = (k%size)
        
        nums[:] = nums[size-k:] + nums[:size-k]