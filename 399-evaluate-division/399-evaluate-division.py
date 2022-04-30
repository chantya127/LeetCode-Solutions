from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        def solve(src , dest):
            
            ans = [-1]
            
            def dfs(node , cost):
                
                if (node == dest):
                    ans[0] = cost
                    return 
                
                if (node in vis or ans[0] != -1):
                    return 
                
                vis.add(node)
                
                for (adj, wt) in graph[node]:
                    
                    dfs(adj , cost*wt)
                
            
            
            if (src == dest):
                return(1.00000)
            
            vis = set()
            for adj,wt in graph[src]:
                
                if (adj not in vis):
                    dfs(adj , wt)
                
                if (ans[0] != -1):
                    break
            
            if (ans[0] != -1):
                return(ans[0])
            
            else:
                return (-1.00000)
                

        graph = defaultdict(list)
        nodes = set()
        for i in range(len(equations)):
            
            u,v,wt = equations[i][0],equations[i][1] , values[i]
            
            graph[u].append((v,wt))
            graph[v].append((u , 1/wt))
            nodes.add(u)
            nodes.add(v)
        
        ans = []
        for i in range(len(queries)):
            
            src,dest = queries[i][0] , queries[i][1]
            if (src not in nodes or dest not in nodes):
                ans.append(-1.00000)
            else:
                ans.append(solve(src , dest))
                
        return (ans)    
            
            
        