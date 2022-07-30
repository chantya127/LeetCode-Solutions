class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        print(nums)
        
        size = len(nums)
        for p1 in range(size-2):
            
            
            if (p1 >0 and nums[p1] == nums[p1-1]):
                continue
                
            n1 = nums[p1]
            
            p2 , p3 = p1+1 , size-1
            
            while(p2 < p3):
                
                curr_sum = nums[p1] + nums[p2] + nums[p3]

                if (curr_sum == 0):
                    
                    ans.append([nums[p1] , nums[p2] , nums[p3]])
                    
                    p2 +=1
                    while(p2 < p3 and nums[p2] == nums[p2-1]):
                        p2 +=1
                    
                    p3 -=1
                    while(p3 >=0 and nums[p3] == nums[p3+1]):
                        p3 -=1
                
                elif (curr_sum <0):
                    p2 +=1
                
                else:
                    p3 -=1
        
        return (ans)
                