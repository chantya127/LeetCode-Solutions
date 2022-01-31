class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ans = []
        
        p1 , p2 = 0,0
        
        while(p1<m and p2 < n):
            
            v1,v2= nums1[p1] , nums2[p2]
            
            if (v1 < v2):
                ans.append(v1)
                p1 +=1
            
            else:
                ans.append(v2)
                p2 +=1
        
        while(p1 <m):
            ans.append(nums1[p1])
            p1 +=1
        
        while(p2 < n):
            ans.append(nums2[p2])
            p2 +=1
        
        nums1[:] = ans[:]