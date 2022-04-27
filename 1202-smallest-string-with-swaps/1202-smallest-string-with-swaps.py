class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def find_adj(node , comp):
            
            comp.append(node)
            vis[node] = 1
            
            for adj in graph[node]:
                if (vis[adj] == 0):
                    find_adj(adj , comp)
                    
        
        size = len(s)
        
        lst = list(s)
        
        graph = defaultdict(list)
        
        for (u,v) in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        
        vis = [0]*(size)
        
        for node in range(size):
            if (vis[node] == 0):
                
                comp = []
                find_adj(node , comp)
                
                comp.sort()
                chars = [lst[ch] for ch in comp]
                chars.sort()
                
                for idx in range(len(comp)):
                    lst[comp[idx]] = chars[idx]
        
        return (''.join(lst))
                    
                    
                
            
        