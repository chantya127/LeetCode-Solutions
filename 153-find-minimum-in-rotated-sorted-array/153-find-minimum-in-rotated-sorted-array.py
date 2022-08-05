class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        size = len(nums)
        low, high = 0 , size-1
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            
            print(low , mid, high)
            
            if (mid >0 and nums[mid-1] > nums[mid]):
                return (nums[mid])
            
            if (mid +1 < size and nums[mid] > nums[mid+1]):
                return nums[mid+1]
            
            if (nums[mid] < nums[high]):
                high = mid-1
            
            else:
                low = mid+1
        
        
        return nums[0]
            
    
    # [3,4,5,6,7,1,2]