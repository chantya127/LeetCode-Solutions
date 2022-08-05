class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def solve(row, col):
            
            grid[row][col] = '0'
            
            for (a,b) in dirs:
                
                nrow , ncol = row+a , col+b
                
                if (0 <= nrow < row_size and 0 <= ncol < col_size and grid[nrow][ncol] == '1'):
                    solve(nrow, ncol)
                    
        
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]
        row_size , col_size = len(grid) , len(grid[0])
        
        islands = 0
        
        for r in range(row_size):
            for c in range(col_size):
                if (grid[r][c] == '1'):
                    islands +=1
                    solve(r,c )
        
        return (islands)