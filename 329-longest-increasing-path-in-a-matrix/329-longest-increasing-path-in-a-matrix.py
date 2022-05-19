dirs = [(-1,0), (1,0) , (0,-1) , (0,1)]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def is_valid(row,col , nrow,ncol):
            
            if (nrow<0 or nrow >=n or ncol <0 or ncol >=m):
                return False
            
            last = matrix[row][col]
            curr = matrix[nrow][ncol]
            if (curr > last):
                return True
            
            return False
            
        
        def solve(row, col):
            if (row <0 or row >=n or col<0 or col>=m):
                return 0
            
            # if (row ==n-1 and col == m-1):
            #     dp[row][col]= 1
            #     return 1
            
            if (dp[row][col] != -1):
                return dp[row][col]
            
            ans = 0
            
            for (a,b) in dirs:
                
                nrow , ncol = row+a, col+b
                if (is_valid(row,col , nrow,ncol)):
                    
                    val = solve(nrow ,ncol)
                    ans = max(ans ,val)
            
            dp[row][col] = ans+1
            return (ans+1)
            
            
            
        
        n , m = len(matrix) , len(matrix[0])
        
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                
                if (dp[i][j] == -1):
                    solve(i,j)
                    # if (matrix[i][j] == 0):
                    #     print(res)
                    
                ans = max(ans , dp[i][j])
        
#         for row in dp:
#             print(row)
            
        return (ans)