class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = float('inf')
        profit = 0
        
        for price in prices:
            
            mini = min(mini , price)
            curr_profit = price -mini
            profit = max(profit , curr_profit)
        
        return (profit)