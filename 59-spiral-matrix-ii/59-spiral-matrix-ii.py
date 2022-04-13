class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        m = n
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        start = 1
        
        left ,right = 0 , m-1
        up,bottom = 0, n-1
        
        turn = 0
        
        while(left<=right and up<= bottom):
            
            
            if (turn == 0): # left to right
                
                for i in range(left ,right+1,1):
                    
                    (matrix[up][i]) = start
                    start +=1
                
                up+=1
                
            
            elif (turn == 1): # up->bot
                
                for i in range(up,bottom+1 ,1):
                    (matrix[i][right]) = start
                    start +=1
                
                right -=1
                
            
            elif (turn == 2): # right -> left
                
                for j in range(right ,left-1,-1):
                    (matrix[bottom][j]) = start
                    start +=1
                
                bottom -=1
            
            else: # bottom -> up
                
                
                for i in range(bottom ,up-1,-1):
                    (matrix[i][left]) = start
                    start +=1
                
                left +=1
                
            
            turn = (turn + 1)%4
        
        return matrix