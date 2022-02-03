
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        size = len(nums)
        
        indices = {}
        
        for idx in range(size):
            
            curr = nums[idx]
            
            rem = target - curr
            
            if (rem in indices):
                return [indices[rem] , idx]
            
            if curr not in indices:
                indices[curr] = idx
        
                    