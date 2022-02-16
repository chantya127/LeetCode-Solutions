class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        ququ = deque()
        size = len(nums)
        dp = [0]*(size)
        dp[0] = nums[0]
        ququ.append(0)
        
        for idx in range(1,size,1):
            
            while(ququ and idx-ququ[0] >k):
                ququ.popleft()
            
            curr_sum = dp[ququ[0]] + nums[idx]
            
            while(ququ and dp[ququ[-1]] <= curr_sum):
                ququ.pop()
                
            dp[idx] = curr_sum
            ququ.append(idx)
        
        return dp[-1]
