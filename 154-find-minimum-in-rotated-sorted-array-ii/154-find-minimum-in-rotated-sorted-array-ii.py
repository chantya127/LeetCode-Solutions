class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        
        low= 0
        high = size-1
        
        while(low < high):
            
            mid = (high-low)//2 + low
            
            #print(nums[mid] , mid,  low,high)
            
            if (nums[mid] <= nums[high]):
                
                if (nums[mid] != nums[high]):
                    high = mid
                
                else:
                    high = high-1
            
            else:
                low = mid+1
        
        return nums[low]