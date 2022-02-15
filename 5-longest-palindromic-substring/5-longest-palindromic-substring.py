class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start ,maxlen = 0,1
        
        size = len(s)
        
        for idx in range(1,size):
            
            #even length
            low = idx-1
            high = idx
            
            while(low >=0 and high < size and s[low] == s[high]):
                if(high-low +1 > maxlen):
                    
                    maxlen = high-low+1
                    start = low
                high +=1
                low -=1
            
            # odd length
            low = idx-1
            high = idx+1
            
            while(low >=0 and high < size and s[low] == s[high]):
                if(high-low +1 > maxlen):
                    
                    maxlen = high-low+1
                    start = low
                high +=1
                low -=1
        
        return s[start:start + maxlen]