class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def poss(target):
            
            summe = nums[0]
            count = 1
            
            for num in nums[1:]:
                
                summe += num
                if (summe >target):
                    count +=1
                    summe = num
                
                if (count >m):
                    break
            
            return (count <=m)
                    
            
        
        size = len(nums)
        
        prefix = [nums[idx] for idx in range(size)]
        
        for idx in range(1,size):
            prefix[idx] += prefix[idx-1]
        
        
        low = max(nums)
        high =sum(nums)
        
        ans = 0
        
        while(low <= high):
            
            mid = (high -low)//2 + low
            
            if (poss(mid)):
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)
    
