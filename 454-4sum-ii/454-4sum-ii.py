from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        
        count = defaultdict(int)
        
        for n1 in nums1:
            for n2 in nums2:
                
                summe = n1+n2
                count[summe] +=1
        
        ans = 0
        for n3 in nums3:
            
            for n4 in nums4:
                
                summe = n3+n4
                if -(summe)in count:
                    ans += count[-summe]
            
        return (ans)