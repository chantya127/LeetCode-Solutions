class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        size = len(arr)
        
        if (size < 3):
            return False
        
        idx = 0
        
        while(idx <size-1 and arr[idx] < arr[idx+1]):
            idx +=1
        
        if (idx == 0 or idx == size-1):
            return (False)
        
        while(idx <size-1 and arr[idx] > arr[idx+1]):
            idx +=1
        
        return (idx == size-1)