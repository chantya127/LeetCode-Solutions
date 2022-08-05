from collections import defaultdict

class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        
        def solve(node , graph):
            
            if (vis[node] == 1):
                return True
            
            vis[node] = 1
            for adj in graph[node]:
                if (vis[adj] == 0):
                    val = solve(adj , graph)
                    if (val):
                        return True
                
                elif(vis[adj] == 1):
                    return True
            
            vis[node] = 2
            return False
        
        graph = defaultdict(list)
        
        for (dest,src) in pre:
            graph[src].append(dest)
        vis = [0]*(num)
        
        for idx in range(num):
            if (vis[idx] == 0):
                check = solve(idx , graph)
                if (check):
                    return False
        
        return True