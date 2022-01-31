class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def swap(matrix , r1,c1 , r2,c2):
            
            matrix[r1][c1] , matrix[r2][c2] = matrix[r2][c2] , matrix[r1][c1]
        
        size = len(matrix)
        
        for r in range(size):
            for c in range(r+1,size,1):
                
                swap(matrix , r,c , c,r)
        
        
        st,end = 0 ,size-1
        
        while(st < end):
            
            for row in range(size):
                
                swap(matrix , row,st , row,end)
            
            st +=1
            end -=1