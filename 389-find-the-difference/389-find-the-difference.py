class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        mark = [0]*(26)
        
        for ch in s:
            
            idx = ord(ch) - ord('a')
            mark[idx] +=1
        
        for ch in t:
            
            idx =ord(ch) - ord('a')
            if(mark[idx] == 0):
                return ch
            
            else:
                mark[idx] -=1