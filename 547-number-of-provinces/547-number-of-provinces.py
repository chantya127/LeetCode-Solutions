from collections import defaultdict

class Solution:
    def findCircleNum(self, connected: List[List[int]]) -> int:
        
        def solve(node , vis):
            
            vis[node] = 1
            for adj in graph[node]:
                if (vis[adj] == 0):
                    solve(adj ,vis)
        
        
        graph = defaultdict(list)
        
        nodes = len(connected)
        
        for src in range(nodes):
            for adj in range(nodes):
                
                if(connected[src][adj]):
                    graph[src].append(adj)
                    graph[adj].append(src)
        
        count = 0
        vis = [0]*(nodes)
        
        for node in range(nodes):
            if (vis[node] == 0):
                
                solve(node , vis)
                count +=1
        
        return (count)
                