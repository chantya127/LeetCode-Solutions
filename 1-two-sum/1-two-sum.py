from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        vis = defaultdict(int)
        
        for (idx , num) in enumerate(nums):
            if (target - num) in vis:
                # print(target , num , idx , vis)
                return [vis[target-num] , idx]
            
            vis[num] = idx
        