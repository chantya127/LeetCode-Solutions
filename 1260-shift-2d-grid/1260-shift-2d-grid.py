class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        row_size , col_size = len(grid) , len(grid[0])
        size = row_size*col_size
        
        new_grid = [[-1 for _ in range(col_size)] for _ in range(row_size)]
        
        curr_pos = 0
        
        for row in range(row_size):
            for col in range(col_size):
                
                curr_ele = grid[row][col]
                
                next_idx = (curr_pos + k) % size
                
                new_row , new_col = (next_idx)//col_size , next_idx%col_size
                
                new_grid[new_row][new_col] = curr_ele
                
                curr_pos +=1
        
        return (new_grid)
                