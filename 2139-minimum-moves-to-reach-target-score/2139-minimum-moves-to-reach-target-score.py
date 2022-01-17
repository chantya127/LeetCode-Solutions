class Solution:
    def minMoves(self, target: int, maxi: int) -> int:
        
        @lru_cache(None)
        def solve(curr ,doubles):
            
            if (curr == 1):
                return 0
            
            
            v1 = float('inf')
            
            if (doubles >0)and (curr//2 >0):
                
                if ((curr%2 == 0)):
                    v1 = solve(curr//2 , doubles-1)+1
                
                else:
                    v1 = solve(curr-1 , doubles)+1
            
            else:            
                v1 = curr-1
            
            return (v1)
                
            
        
        moves = solve(target,maxi)        
        
        return (moves)