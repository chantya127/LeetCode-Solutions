class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        size = len(grid)
        zeros = []
        
        for row in range(size):
            
            count_zeros= size
            
            for col in range(size-1,-1,-1):
                
                curr = grid[row][col]
                if (curr == 1):
                    
                    count_zeros = size -col-1
                    break
            
            zeros.append(count_zeros)
        
        ans = 0
        
        for row in range(size):
            
            target = size-row-1
            
            if (zeros[row] < target):
                
                ptr = row+1
                while(ptr<size and zeros[ptr] < target):
                    
                    ptr +=1
                
                if (ptr == size):
                    return -1
                
                while(ptr > row):
                    zeros[ptr] , zeros[ptr-1] = zeros[ptr-1] , zeros[ptr]
                    ptr -=1
                    ans +=1
                    
        return (ans)