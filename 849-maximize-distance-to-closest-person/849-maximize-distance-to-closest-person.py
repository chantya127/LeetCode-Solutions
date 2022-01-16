class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        size = len(seats)
        k = 0
        ans = 0
        
        for idx in range(size):
            if (seats[idx] == 1):
                k = 0
            
            else:
                k +=1
                ans = max(ans , (k+1)//2)
        
        for idx in range(size):
            if (seats[idx] == 1):
                ans = max(ans , idx)
                break
        
        for idx in range(size-1,-1,-1):
            if (seats[idx] == 1):
                ans = max(ans , size-idx-1)
                break
            
        return (ans)