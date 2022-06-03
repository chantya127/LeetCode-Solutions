class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        
        n , m = len(matrix) , len(matrix[0])
        self.rows = n
        self.cols = m
        
        self.matrix = [[0 for _ in range(m)] for  _ in range(n)]
        
        for i in range(n):
            self.matrix[i] = matrix[i]
        
        for j in range(1,m):
            for i in range(n):
                self.matrix[i][j]+=self.matrix[i][j-1]
        
        for i in range(1,n):
            for j in range(m):
                self.matrix[i][j]+=self.matrix[i-1][j]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        ans = self.matrix[row2][col2]
        d1,d2= 0 , 0
        add = 0
        
        if row1 >0:
            d1 = self.matrix[row1-1][col2]
        
        if col1 > 0:
            d2 = self.matrix[row2][col1-1]
        
        if row1 >0 and col1 >0:
            add = self.matrix[row1-1][col1-1]
        
        return (ans + add -d1 -d2)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)