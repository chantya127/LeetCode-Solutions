class Solution:
    
    def valid(self ,  row ,col ,grid ,n):
            
            if row<0 or col<0 or row>=n or col>=n or grid[row][col] ==1:
                return False
            
            for i in range(n):
                if grid[i][col] == 1:
                    return False
            
            for j in range(n):
                if grid[row][j] == 1:
                    return False
            
            i,j = row ,col
            while(i>=0 and j>=0):
                
                if grid[i][j] == 1:
                    return False
                
                i-=1
                j-=1
                
            i,j = row , col
            while (i>=0 and j<n):
                if grid[i][j] ==1:
                    return False
                
                i-=1
                j+=1
                
            return True
    
    def totalNQueens(self, n: int) -> int:
            
        
        def solve(grid , nrow  ,res):
            
            if nrow == n:
                
                res[0]+=1

            
            for ncol in range(n):
                
                if self.valid(nrow , ncol ,grid ,n):
                    
                    grid[nrow][ncol] = 1
                    solve(grid , nrow+1  ,res)
                    grid[nrow][ncol] = 0
                    
                
            
            
        
        if n ==1:
            return 1
        
        grid = [[0 for _ in range(n)] for _ in range(n)]
        
        res = [0]
        
        solve(grid , 0  ,res) 
        
        return res[0]