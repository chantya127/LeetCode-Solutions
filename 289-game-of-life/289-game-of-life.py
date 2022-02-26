class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def count(row,col):
            
            curr = 0
            for (a,b) in dirs:
                nrow,ncol = row+a, col+b
                
                if (0 <= nrow< row_size and 0 <= ncol < col_size):
                    if (board[nrow][ncol] ==1 or board[nrow][ncol] == die):
                        curr +=1
            
            return (curr)
        
        row_size ,col_size = len(board) , len(board[0])
        
        live = 3
        die = 2
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1) , (-1,-1) , (1,-1) , (1,1) , (-1,1)]
        for r in range(row_size):
            for c in range(col_size):
                
                around = count(r,c)
                if (board[r][c] == 0 and around ==3):
                    board[r][c] = live
                
                if (board[r][c]== 1):
                    if (around <2 or around > 3):
                        board[r][c] = die
            
        for r in range(row_size):
            for c in range(col_size):
                if (board[r][c] == die):
                    board[r][c] = 0
                
                if (board[r][c] == live):
                    board[r][c] = 1
                    