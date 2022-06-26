class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        size = len(cardPoints)
        
        summe = 0
        for idx in range(k):
            summe+= cardPoints[idx]
        
        ans = summe
        if (size == k):
            return ans
        
        for idx in range(k):
            
            summe = summe - cardPoints[k-idx-1] + cardPoints[size-idx-1]
            
            if(summe)> ans:
                ans = summe
        
        return (ans)