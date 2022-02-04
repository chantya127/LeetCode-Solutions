class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        ans = 0
        summe = 0
        
        indices = {summe :-1}
        
        for end in range(size):
            
            num = nums[end]
            
            if (num ==0):
                summe -=1
            
            else:
                summe +=1
            
            if (summe in indices):
                
                st = indices[summe]
                length = end -st
                ans = max(ans  , length)
                
            else:
                indices[summe] = end
        return(ans)
        