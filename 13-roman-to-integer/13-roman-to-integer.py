class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping =  {'I' :1,'V': 5, 'X': 10, 'L' :50,'C': 100, 'D' : 500, 'M':1000}
        
        ptr = 0
        ans = 0
        size = len(s)
        
        while(ptr < size):
            
            curr = mapping[s[ptr]]
            nexa = 0
            
            if(ptr+1 < size):
                nexa = mapping[s[ptr+1]]
            
            if (nexa > curr):
                ans += nexa -curr
                ptr +=2
            
            else:
                ans += curr
                ptr+=1
        
        return ans