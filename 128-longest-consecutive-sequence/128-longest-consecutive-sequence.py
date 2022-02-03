class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        vis = set(nums)
        ans = 0
        
        for num in vis:
            
            if (num-1 not in vis):
                
                count = 1
                temp = num
                while(temp+1 in vis):
                    
                    temp +=1
                    count +=1
                
                ans = max(ans, count)
        
        return (ans)