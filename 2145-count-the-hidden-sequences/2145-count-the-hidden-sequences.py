class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        
        size = len(diff)
        prefix = [0]*(size+1)
        
        prefix[1] = diff[0]
        maxi , mini = prefix[1] , prefix[1]
        
        for i in range(2,size+1,1):
            
            prefix[i] += prefix[i-1] + diff[i-1]
            maxi = max(maxi , prefix[i])
            mini = min(mini , prefix[i])
        
        count = 0

        for i in range(lower , upper+1 ,1):
            
            if ((lower <= i+mini <=upper) and (lower <= i+maxi <= upper) ):
                count +=1
        
        return (count)