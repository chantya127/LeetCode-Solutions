class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        limit = (size)//3
        c1 , majority_ele1 = 0,float('inf')
        
        c2 , majority_ele2 = 0,float('inf')
        
        for idx in range(size):
            
            curr = nums[idx]
            
            if (c1 == 0 or curr == majority_ele1 )and curr != majority_ele2:
                c1 += 1
                majority_ele1 = curr
            
            elif(c2 == 0 or curr == majority_ele2):
                c2 += 1
                majority_ele2 = curr
            
            else:
                c1 -=1
                c2 -=1
        
        ans = []
        
        new_c1 ,new_c2 = 0,0
        # print(majority_ele1 , majority_ele2)
        for num in nums:
            if (num == majority_ele1):
                new_c1 +=1
            
            if(num == majority_ele2):
                new_c2 +=1
        
        if (new_c1 > limit):
            ans.append(majority_ele1)
        
        if(new_c2 > limit):
            ans.append(majority_ele2)
        
        return (ans)