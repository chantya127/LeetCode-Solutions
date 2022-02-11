# from collections import default

class Solution:
    def checkInclusion(self, x: str, y: str) -> bool:
        
        def compare(arr1 , arr2):
            
            for idx in range(limit):
                
                if (arr1[idx] != arr2[idx]):
                    return False
            
            return True
        
        
        
        s1,s2 = len(x) , len(y)
        if (s1 > s2):
            return  False
        
        limit = 26
        mp1 = [0]*(26)
        mp2 = [0]*(26)
        
        for idx in range(s1):
            
            ch = x[idx]
            asci = ord(ch) -ord('a')
            mp1[asci] +=1
            
            ch2 = y[idx]
            asci2 = ord(ch2) - ord('a')
            mp2[asci2] +=1
        
        for idx in range(s1,s2,1):
            
            if (compare(mp1,mp2)):
                return True
            
            curr = ord(y[idx]) -ord('a')
            mp2[curr] +=1
            
            prev = ord(y[idx-s1]) -ord('a')
            mp2[prev] -=1
        
        if(compare(mp1,mp2)):
            return True
        
        return False
        