class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        size = len(nums)
        if (size == 1):
            return nums[0]
        
        low = 0
        high = size-1
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            
            if (mid+1 <size and nums[mid] != nums[mid+1] and (mid == 0 or nums[mid-1]!= nums[mid])):
                return nums[mid]
            
            if (mid-1 >=0 and nums[mid] != nums[mid-1] and (mid == size-1 or nums[mid+1] != nums[mid])):
                return nums[mid]
            
            # first element amongst two
            elif(mid+1 <size and nums[mid] == nums[mid+1]):
                
                if (mid%2 ==0):
                    low = mid+2
                
                else:
                    high = mid-1
                    
            # second element
            else:
                if (mid%2 == 0):
                    high = mid-2
                
                else:
                    low = mid+1
                
                    
                