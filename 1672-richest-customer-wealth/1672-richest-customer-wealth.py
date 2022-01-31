class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        ans = 0
        for wealth in accounts:
            
            summe = sum(wealth)
            if (summe > ans):
                ans = summe
        
        return (ans)