class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(arr , p1,p2):
            if (p1 != p2):
                arr[p1] = arr[p1]^arr[p2]
                arr[p2] = arr[p1]^arr[p2]
                arr[p1] = arr[p1]^arr[p2]
        
        size = len(nums)
        
        st ,end = 0 , size-1
        mid = 0
        
        while(mid <= end):
            
            curr = nums[mid]
            
            if(curr == 0):
                
                swap(nums , st ,mid)
                st +=1
                mid +=1
            
            elif(curr == 2):
                swap(nums , end , mid)
                end -=1
            
            else:
                mid +=1