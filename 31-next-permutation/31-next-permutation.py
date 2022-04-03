class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        size = len(nums)
        flag = 0
        
        for k in range(size-2,-1,-1):
            if(nums[k+1] > nums[k]):
                flag = 1
                break
                
        if(flag):
            
            for idx in range(size-1,-1,-1):
                
                if (nums[idx] > nums[k]):
                    break
            
            nums[idx] , nums[k] = nums[k] ,nums[idx]
            k+=1
            
        else:
            k = 0
            
        start = k
        end = size-1
        while(start < end):
            nums[start] ,nums[end] = nums[end] , nums[start]
            start +=1
            end -=1
        
        