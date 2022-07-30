class Solution:
    def insert(self, intervals: List[List[int]], target: List[int]) -> List[List[int]]:
        
        size = len(intervals)
        
        ans = []
        idx = 0
        
        while(idx < size and intervals[idx][1] < target[0]):
            ans.append(intervals[idx])
            idx +=1
        
        
        while(idx < size and target[1] >= intervals[idx][0]):
            
            target[0] = min(target[0] , intervals[idx][0])
            target[1] = max(target[1] , intervals[idx][1])
            
            idx +=1
        
        ans.append(target)
        while(idx < size):
            ans.append(intervals[idx])
            idx +=1
        
        return (ans)