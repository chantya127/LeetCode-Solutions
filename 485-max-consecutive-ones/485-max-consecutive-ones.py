class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = 0
        size = len(nums)
        ptr = 0
        
        while(ptr < size):
            
            if (nums[ptr] ==1):
                
                st = ptr
                while(ptr < size and nums[ptr] == 1):
                    ptr +=1
                
                curr_length = ptr - st
                ans = max(ans , curr_length)
            
            ptr +=1
        
        return ans
            