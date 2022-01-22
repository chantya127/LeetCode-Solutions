class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def solve(row,col , matrix , prev):
            
            if (row<0 or row>=row_size or col<0 or col>=col_size or heights[row][col]<prev or matrix[row][col] == 1):
                return 
            
            matrix[row][col] = 1
            
            for (a,b) in dirs:
                
                solve(row+a , col+b , matrix ,heights[row][col])
        
        if (len(heights) == 0):
            return []
        
        row_size,col_size = len(heights) , len(heights[0])
        
        at = [[0 for _ in range(col_size)] for _ in range(row_size)]
        
        pac = [[0 for _ in range(col_size)] for _ in range(row_size)]
        
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]
        
        # left and right row each for pacific and atlantic
        for row in range(row_size):
            
            solve(row , 0 , at , float('-inf'))
            solve(row, col_size-1 , pac , float('-inf'))
        
        
        # top and bottom column
        for col in range(col_size):
            solve(0 , col , at  ,float('-inf'))
            solve(row_size-1 , col , pac , float('-inf'))
            
        ans = []
        
        for row in range(row_size):
            for col in range(col_size):
                if (at[row][col] and pac[row][col]):
                    ans.append([row,col])
        
        return (ans)