class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def solve(low , high):
            
            if (low+1 == high):
                return (0)
            
            ans = 0
            
            for idx in range(low+1 ,high,1):
                
                temp = solve(low , idx) + solve(idx,high)
                
                lt,rt = nums[low] , nums[high]
                
                temp += nums[idx]*lt*rt
                
                ans = max(ans , temp)
            
            return (ans)
                
        nums.insert(0,1)
        nums.append(1)
        
        size = len(nums)
        
        ans = solve(0 ,size-1)
        
        return (ans)