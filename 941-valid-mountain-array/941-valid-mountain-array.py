class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        size = len(arr)
        
        if (size < 3):
            return False
        
        maxi = -1
        idx = -1
        
        for i in range(size):
            
            curr = arr[i]
            if (curr > maxi):
                maxi = curr
                idx = i
        
        left= idx-1
        
        right = idx+1
        if (left <0 or right >= size):
            return False
        
        prev = maxi
        for idx in range(left , -1,-1):
            
            curr = arr[idx]
            if (curr >= prev):
                return False
            
            prev = curr
        
        prev = maxi
        for idx in range(right , size,1):
            curr = arr[idx]
            if (curr >=  prev):
                return False
            
            prev = curr
        
        return (True)