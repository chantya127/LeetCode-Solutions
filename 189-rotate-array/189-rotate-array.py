class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k= (k%size)
        
        ans = [0]*(size)
        
        for idx in range(size):
            
            next_idx = (idx + k)%size
            ans[next_idx] = nums[idx]
        
        nums[:] = ans[:]