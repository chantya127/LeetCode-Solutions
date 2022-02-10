class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        summe = 0
        dd = defaultdict(int)
        dd[summe]  =1
        count = 0
        
        for num in nums:
            
            summe +=num
            
            if (summe -k in dd):
                count += dd[summe-k]
            
            dd[summe]+=1
        
        return count