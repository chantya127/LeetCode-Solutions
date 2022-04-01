class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        size  = len(s)
        
        low = 0
        high = size-1
        while(low < high):
            
            s[low] , s[high] = s[high] , s[low]
            
            low +=1
            high -=1