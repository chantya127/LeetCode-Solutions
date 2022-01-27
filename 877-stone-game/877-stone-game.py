class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def solve(left , right):
            
            if (left > right):
                return 0
            
            if (left == right):
                return piles[left]
            
            if (left +1 == right):
                
                return max(piles[left] , piles[right])
            
            v1 = piles[left] + min(solve(left+2 , right) , solve(left+1 , right-1))
            v2 = piles[right] + min(solve(left , right-2) , solve(left + 1 , right-1))
            
            return max(v1,v2)
        
        summe = sum(piles)
        size = len(piles)
        alice = solve(0 , size-1)
        
        bob = summe - alice
        
        return (alice > bob)
        