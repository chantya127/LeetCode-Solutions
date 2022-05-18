from collections import defaultdict

timer = 0

class Solution:
    
    def solve(self , graph , u , disc , low , parent , ans):
        
        global timer 
        
        disc[u] = timer
        low[u] = timer
        timer+=1
        for v in graph[u]:
            if disc[v] == -1:
                parent[v] = u
                self.solve(graph , v , disc , low ,parent , ans)
                low[u] = min(low[v] , low[u])
                if low[v] > disc[u]:
                    ans.append((u,v))
            
            elif (v != parent[u]):
                low[u] = min(low[u], disc[v])
        
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for (src,dest) in connections:
            graph[src].append(dest)
            graph[dest].append(src)
        
        ans = []
        disc= [-1]*(n)
        low = [-1]*(n)
        parent =[-1]*(n)
        global timer
        
        for i in range(n):
            if disc[i] == -1:
                self.solve(graph , i ,  disc , low ,parent , ans)
                
        return ans        
        