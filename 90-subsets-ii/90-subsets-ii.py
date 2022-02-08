class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def solve(idx , curr):
            
            ans.append(curr[:])
            
            for pos in range(idx , size):
                
                if (pos > idx and nums[pos] == nums[pos-1]):
                    continue
                
                else:
                    curr.append(nums[pos])
                    solve(pos+1 , curr)
                    curr.pop()
            
        ans = []
        size = len(nums)
        nums.sort()
        solve(0 , [])

        
        return (ans)