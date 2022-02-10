class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_valid(row,col ,board ,poss):
            
            for idx in range(size):
                
                # print(board[row][idx] , board[idx][col] , poss, board[idx][col]== poss)
                
                if (board[row][idx] == poss) or (board[idx][col] == poss):
                    return False
            
            tp_row = (row//3)*3
            tp_col = (col//3)*3
            
            for r in range(tp_row,tp_row+3 , 1):
                for c in range(tp_col , tp_col+3 , 1):
                    
                    if(board[r][c] == poss):
                        return False
            
            return (True)
        
        def solve(row,col,board):
            
            if (row == size):
                return True
            
            if(col == size-1):
                ncol = 0
                nrow = row+1
            
            else:
                nrow = row
                ncol = col+1
            
            if(board[row][col] != '.'):
                return solve(nrow,ncol,board)
            
            else:
                
                for poss in range(1,10):
                    poss = str(poss)
                    if (is_valid(row,col , board,poss)):
                        board[row][col] = poss

                            
                        if(solve(nrow,ncol,board)):
                            return True
                        
                        board[row][col] ='.'
                
                return False
            
        size = len(board)
        
        val = solve(0,0,board)
        
        
        
        return board