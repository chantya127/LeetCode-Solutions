class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        size = len(nums)
        low = 0
        high = size-1
        
        while(low <= high):
            mid = (high-low)//2 + low
            
            if (nums[mid] == target):
                return True
            
            if (nums[low] < nums[mid]):
                
                if (nums[low] <= target and target <= nums[mid]):
                    high = mid-1
                
                else:
                    low = mid+1
            
            elif(nums[mid] < nums[high]):
                if (nums[mid] <= target and target <= nums[high]):
                    low = mid+1
                
                else:
                    high = mid-1
                
            else:
                if (nums[mid] == nums[low]):
                    low+=1
                
                if (nums[mid] == nums[high]):
                    high -=1
        
        return False