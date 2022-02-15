
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ququ = deque()
        fresh = 0
        
        row_size,col_size = len(grid), len(grid[0])
        
        for r in range(row_size):
            for c in range(col_size):
                
                if (grid[r][c] == 1):
                    fresh +=1
                
                elif(grid[r][c] == 2):
                    ququ.append((r,c))
        
        time = 0
        dirs = [(-1,0) ,(1,0) , (0,-1) , (0,1)]
        
        while(ququ and fresh>0):
            
            time +=1
            size = len(ququ)
            
            for _ in range(size):
                
                r,c = ququ.popleft()
                for (a,b) in dirs:
                    nrow,ncol = r+a , c+b
                    
                    if (0 <= nrow <row_size and 0 <= ncol <col_size and grid[nrow][ncol] == 1):
                        fresh -=1
                        grid[nrow][ncol] = 2
                        
                        ququ.append((nrow,ncol))
        
        if (fresh ==0):
            return (time)
        
        else:
            return -1