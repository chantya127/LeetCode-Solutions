class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        size = len(nums)
        if (size < 4):
            return []
        
        nums.sort()
        ans = []
        
        for p1 in range(size-3):
            
            if (p1 >0 and nums[p1] == nums[p1-1]):
                continue
            
            for p2 in range(p1+1,size-2):
                
                if (p2 >p1+1 and nums[p2] == nums[p2-1]):
                    continue
                
                p3 = p2+1
                p4 = size-1
                
                while(p3 < p4):
                    
                    summe = nums[p1] + nums[p2] +nums[p3] + nums[p4]
                    
                    if(summe == target):
                        ans.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                    
                        curr = nums[p3]
                        while(p3 < p4 and nums[p3] == curr):
                            p3 +=1

                        curr =nums[p4]
                        while(p3 < p4 and nums[p4] == curr):
                            p4 -=1
                        
                    elif (summe > target):
                        p4-=1
                    
                    else:
                        p3 +=1
                
        
        return (ans)
                
                
                
                