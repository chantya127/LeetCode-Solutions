from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        
        def find_min(dis , vis):
            
            index , val = -1 , float('inf')
            for i in range(1,n+1):
                if not vis[i] and val > dis[i]:
                    val =  dis[i]
                    index = i
            
            return index
            
        
        graph = defaultdict(list)
        for i in times:
            u,v,time = i[0] , i[1] , i[2]
            graph[u].append((v,time))
        
        dis = [float('inf')]*(n+1)
        dis[src] = 0
        vis = [0]*(n+1)
        for i in range(n-1):
            
            u = find_min(dis , vis)
            
            vis[u] = 1
            for (v,t) in graph[u]:
                
                if not vis[v] and dis[v] > dis[u] + t:
                    dis[v] = dis[u] + t
                    
            # print(u , dis)        
        
        maxi = max(dis[1:])
        return maxi if maxi != float('inf') else -1