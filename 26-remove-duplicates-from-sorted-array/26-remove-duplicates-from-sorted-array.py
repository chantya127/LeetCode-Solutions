class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        if (size<2):
            return size
        
        slow,fast = 1,1
        
        while(fast < size):
            
            if(nums[slow-1] != nums[fast]):
                nums[slow] = nums[fast]
                
                #print(nums[slow],slow , nums)
                slow +=1
            
            fast +=1
        
        #print(slow , nums)
        return (slow)