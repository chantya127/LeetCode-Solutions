
from bisect import bisect_left as bl

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        arr =[]
        
        for num in nums:
            
            if (len(arr) == 0 or arr[-1] < num):
                arr.append(num)
            
            else:
                idx = bl(arr , num)
                arr[idx] = num
        
        return len(arr)