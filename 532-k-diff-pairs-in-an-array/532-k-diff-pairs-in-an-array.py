class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        vis = set()
        # nums = list(set(nums))
        
        count = defaultdict(int)
        count[nums[0]] = 1
        ans = 0
        size = len(nums)
        for idx in range(1,size):
            
            curr = nums[idx]
            
            if (curr-k in count) and (curr,curr-k) not in vis:
                vis.add((curr , curr-k))
                #print(curr , curr-k , 'dddd')
                ans +=1
            
            # nums[i] - nums[j] = k
            if k+curr in count and (k+curr,curr) not in vis:
                vis.add((k+curr , curr))
                #print(curr , k-curr , 'ff')
                ans +=1
                
            count[curr] +=1
            
        return (ans)