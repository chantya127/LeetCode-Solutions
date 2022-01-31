class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        size = len(intervals)
        intervals.sort()
        
        ans = []
        temp = intervals[0]
        
        for idx in range(size):
            
            curr = intervals[idx]
            
            if (temp[-1] < curr[0]):
                ans.append(temp)
                temp = curr
            
            else:
                temp[1] = max(temp[1] , curr[1])
            
        ans.append(temp)
        return (ans)