class Solution:

    
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        t = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(amount+1):
                if i == 0:
                    t[i][j] = float('inf')
                
                if j ==0:
                    t[i][j] = 0
                    
        for i in range(1,n+1):
            for j in range(1,amount+1):
                
                if j >= coins[i-1]:
                    t[i][j] = min(t[i-1][j] , t[i][j-coins[i-1]] + 1)
                    
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][amount] if t[n][amount] != float('inf') else -1
                