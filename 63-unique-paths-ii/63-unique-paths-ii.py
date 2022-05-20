class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            
            if grid[i][0] == 1:
                break
            
            else:
                dp[i][0] = 1
        
        for j in range(m):
            
            if grid[0][j] == 1:
                break
            
            else:
                dp[0][j] =1
                
        
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]
        