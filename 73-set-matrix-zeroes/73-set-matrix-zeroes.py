class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        row_size , col_size = len(matrix), len(matrix[0])
        
        row_flag , col_flag = 0,0
        
        for r in range(row_size):
            for c in range(col_size):
                
                if (matrix[r][c] == 0):
                    
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    
                    if (r == 0):
                        row_flag = 1
                    
                    if (c == 0):
                        col_flag = 1
        
        for r in range(1,row_size):
            for c in range(1,col_size):
                
                if (matrix[0][c] == 0 or matrix[r][0] == 0):
                    matrix[r][c] = 0
        
        if (row_flag):
            for c in range(col_size):
                matrix[0][c] = 0
        
        if (col_flag):
            for r in range(row_size):
                matrix[r][0] = 0