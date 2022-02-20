class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        x1,x2 = intervals[0][0] , intervals[0][1]
        count = 1
        
        for idx in range(1 , len(intervals)):
            
            curr = intervals[idx]
            
            if (curr[0] > x1 and curr[1] > x2):
                count +=1
            
            if (curr[1] > x2):
                x1 = curr[0]
                x2 = curr[1]
        
        return count
            