class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(None)
        def solve(rem):
            
            if (rem == 0):
                return False
            
            sq = int(rem**0.5)+1
            
            for num in range(1,sq):
                
                if not solve(rem - num*num):
                    return True
            
            return False
        
        return solve(n)