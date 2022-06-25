class Solution:
    def checkPossibility(self, arr: List[int]) -> bool:
        n = len(arr)
        c = 0
        if n == 1: return True
        
        for  i in range(n-1):
            if arr[i] > arr[i+1]:
                
                c+=1
                if i == 0:
                    arr[i] = arr[i+1]
                
                elif arr[i-1] <= arr[i+1]:
                    arr[i] = arr[i-1]
                
                else:
                    arr[i+1] = arr[i] 
            
            if c==2:
                return False
        
        return c <= 1