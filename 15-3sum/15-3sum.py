class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        ans = []
        
        if (size< 3):
            return ans
        
        nums.sort()
        for ptr1 in range(size-2):
            
            if (ptr1>0 and nums[ptr1] == nums[ptr1-1]):
                continue
            
            ptr2 = ptr1+1
            ptr3 = size-1
            
            while(ptr2 < ptr3):
                
                summe = nums[ptr1] + nums[ptr2] + nums[ptr3]
                
                if (summe == 0):
                    ans.append([nums[ptr1], nums[ptr2] , nums[ptr3]])
                    
                    curr = nums[ptr2]
                    while(ptr2 <ptr3 and nums[ptr2] == curr):
                        ptr2 +=1
                    
                    curr = nums[ptr3]
                    while(ptr2 < ptr3 and nums[ptr3] == curr):
                        ptr3 -=1
                
                elif(summe > 0):
                    ptr3 -=1
                
                else:
                    ptr2 +=1
                
        return ans