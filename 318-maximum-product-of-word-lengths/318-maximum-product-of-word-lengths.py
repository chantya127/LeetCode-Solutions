class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        ans = 0
        n = len(words)
        mask = [0]*(n)
        
        for i in range(n):
            
            for ch in words[i]:
                
                mask[i] |= 1 << ord(ch) - ord('a')
        
        for i in range(n-1):
            for j in range(i+1,n):
                
                if mask[i] & mask[j] == 0:
                    l1 , l2 = len(words[i]) , len(words[j])
                    ans = max(ans , l1 * l2)
            
        
        return ans            
                    