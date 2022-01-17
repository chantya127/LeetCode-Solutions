class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        size = len(questions)
        dp = [[0,0]]*(size)
        
        # inc ->0 , exc ->1
        
        dp[-1][0] = questions[-1][0]
        
        for idx in range(size-2,-1,-1):
            
            curr_power , next_idx = questions[idx][0] , questions[idx][1] + idx+1
            
            inc = curr_power
            if (next_idx <size):
                inc += max(dp[next_idx])
            
            exc = max(dp[idx+1])
            
            dp[idx] = [inc , exc]
        
        return max(dp[0])
        