class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def valid(row,col,board):
            
            for idx in range(size):
                
                if (board[idx][col] == 'Q' or board[row][idx] == 'Q'):
                    return False
            
            r,c = row,col
            
            while(r >=0 and c >=0):
                if (board[r][c] == 'Q'):
                    return False
                
                r -=1
                c -=1
            
            r,c = row,col
            while(r>=0 and c <size):
                
                if (board[r][c] == 'Q'):
                    return False
                
                r -= 1
                c += 1
                
            
            return (True)
            
        
        def solve(row,board):
            
            if (row == size):
#                 for row in board:
#                     print(row)
                
#                 print()
                curr_ans = []
                
                for r in board:
                    new_board = "".join(ch for ch in r)
                    curr_ans.append(new_board)
                    # print(new_board,  r)
                    
                ans.append(curr_ans)
                return
            
            for col in range(size):
                
                if(valid(row,col , board)):
                    board[row][col] = 'Q'

                    solve(row+1, board)
                    board[row][col] = '.'
        
        size = n
        board = [['.' for _ in range(size)] for _ in range(size)]
        ans = []
        
        solve(0 , board)
        
        return ans
        