class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def find_dis(p1,p2):
            
            xval = (p2[0] - p1[0]) **2
            yval = (p2[1] - p1[1])**2
            
            return (xval + yval)
        
        size = len(points)
        ans = 0
        
        for idx in range(size):
            
            curr = points[idx]
            count = defaultdict(int)
            
            for ptr in range(size):
                
                if (idx != ptr):
                    
                    next_pt = points[ptr]
                    dis = find_dis(curr , next_pt)
                    
                    count[dis] +=1
                    
            # print(idx , count)
            for key in count:
                
                ans += (count[key] * (count[key]-1))
        
        return (ans)