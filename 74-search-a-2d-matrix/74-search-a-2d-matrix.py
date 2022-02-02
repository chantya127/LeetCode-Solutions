class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_size,col_size = len(matrix) , len(matrix[0])
        
        low = 0
        high = (row_size*col_size)-1
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            
            r,c = (mid)//col_size , (mid %col_size) 
            
            val = matrix[r][c]
            
            if (val == target):
                return True
            
            elif(val > target):
                high = mid-1
            
            else:
                low = mid+1
        
        return (False)