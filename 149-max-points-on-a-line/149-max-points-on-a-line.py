class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        ans = 1
        
        size = len(points)
        
        for idx in range(size-1):
            
            samept = 1
            x1,y1 = points[idx][0],points[idx][1]
            dd = defaultdict(int)
            
            for ptr in range(idx+1 , size,1):
                
                x2,y2 = points[ptr][0],points[ptr][1]
                
                y_diff = y2-y1
                x_diff = x2-x1
                
                if (x_diff == 0 and y_diff ==0):
                    samept +=1
                
                elif (x_diff !=0):
                    
                    slope = (y_diff / x_diff)
                    
                    dd[slope] +=1
                else:
                    dd[float('inf')] +=1
                    
            count = 0
            for slope in dd:
                
                count = max(count , dd[slope])
            
            ans = max(ans , count+samept)
        
        return ans
        
        
        