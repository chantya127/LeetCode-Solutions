class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        
        mappings = defaultdict(int)
        
        ans = 0
        for num in nums:
            mappings[num] +=1
        
        for (key,val) in mappings.items():
            
            if (key *2 == target):
                ans += val//2
            
            elif(target - key in mappings):
                
                ans += min(mappings[key] , mappings[target-key])
            
                mappings[key] = 0
                mappings[target-key] = 0
                
            
        return ans