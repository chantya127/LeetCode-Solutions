class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        row_size = len(matrix)
        col_size = len(matrix[0])
        
        top,bottom = 0 , row_size-1
        left,right = 0 , col_size-1
        
        ans = []
        case = 0
        
        while(top <= bottom and left <= right):
            
            
            if (case ==0):
                
                for idx in range(left , right+1 ,1):
                    ans.append(matrix[top][idx])
                
                top +=1
            
            elif(case == 1):
                for idx in range(top , bottom+1,1):
                    ans.append(matrix[idx][right])
                
                right -=1
            
            elif(case ==2):
                for idx in range(right , left-1 , -1):
                    ans.append(matrix[bottom][idx])
                
                bottom -=1
            
            else:
                for idx in range(bottom ,top-1,-1):
                    ans.append(matrix[idx][left])
                
                left +=1
            
            case = (case + 1)%4
        return ans