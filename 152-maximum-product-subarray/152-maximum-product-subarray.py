class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_ans = nums[0]
        
        maxi,mini = nums[0] , nums[0]
        
        for num in nums[1:]:
            if (num < 0):
                maxi , mini = mini , maxi
            
            maxi = max(maxi*num , num)
            mini = min(mini*num , num)
            
            max_ans = max(max_ans , maxi , mini)
        
        return (max_ans)