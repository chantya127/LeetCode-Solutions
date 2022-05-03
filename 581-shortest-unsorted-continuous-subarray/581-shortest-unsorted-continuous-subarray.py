class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        maxi = 9999
        left = maxi
        right = 0
        n = len(nums)
        
        if n==1:
            return 0
        
        maxi = nums[right]
        for i in range(1,n):
            if nums[i] < maxi:
                right = i
            else:
                maxi = nums[i]
        
        left = n-1
        mini = nums[left]
        
        for i in range(n-2,-1,-1):
            if nums[i] > mini:
                left = i
            else:
                mini = nums[i]
                
        if right <left:
            return 0
        return right-left+1