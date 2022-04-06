mod = 10**9 + 7

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        @lru_cache(None)
        def solve(row ,col , cuts):
            
            if (row == row_size or col == col_size):
                return 0
            
            apples_left = dp[row][col]
            if (apples_left < cuts):
                return 0
            
            if (cuts == 1):
                return 1
            
            ans = 0
            for row_cut in range(row+1, row_size,1):
                
                prev_apples = apples_left - dp[row_cut][col]
                
                if (prev_apples > 0 and dp[row_cut][col] >= cuts-1):
                    ans = (ans + solve(row_cut , col , cuts-1))%mod
            
            for col_cut in range(col+1 , col_size,1):
                
                prev_apples = apples_left - dp[row][col_cut]
                if(prev_apples > 0 and dp[row][col_cut] >= cuts-1):
                    ans = (ans + solve(row , col_cut , cuts-1))%mod
            
            return (ans)
        
        row_size = len(pizza)
        col_size = len(pizza[0])
        
        dp = [[0 for _ in range(col_size)] for _ in range(row_size)]
        
        dp[-1][-1] = 1 if pizza[-1][-1] == 'A' else 0
        
        for row in range(row_size-2,-1,-1):
            
            dp[row][-1] += dp[row+1][-1]
            
            if pizza[row][-1] == 'A':
                dp[row][-1] +=1
        
        for col in range(col_size-2 ,-1 ,-1):
            dp[-1][col] += dp[-1][col+1] 
            
            if pizza[-1][col] == 'A':
                dp[-1][col] +=1
            
        for row in range(row_size-2, -1,-1):
            for col in range(col_size-2,-1,-1):
                
                dp[row][col] = dp[row+1][col] + dp[row][col+1] - dp[row+1][col+1]
        
                if (pizza[row][col] == 'A'):
                    dp[row][col] += 1
        
        ans = solve( 0,  0 ,k)
        
        return ans