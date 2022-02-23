from collections import defaultdict


class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, vertices, adj, src):
        #code here
        
        def find_min(dis,vis):
            
            min_node , min_val = -1,float('inf')
            
            for idx in range(vertices):
                if (dis[idx] < min_val) and vis[idx] == 0:
                    min_val = dis[idx]
                    min_node = idx
            
            return (min_node)
        
        graph = defaultdict(list)
        
        for (u) in range(vertices):
            
            for (v,wt) in adj[u]:
                graph[u].append((v,wt))
                graph[v].append((u,wt))
        
        dis = [float('inf') for _ in range(vertices)]
        vis = [0 for _ in range(vertices)]
        dis[src] = 0
        
        count = vertices-1
        while(count):
            
            min_node = find_min(dis,vis)
            vis[min_node] = 1
            
            for adj_node,wt in graph[min_node]:
                
                if (dis[adj_node] > dis[min_node] + wt) :
                    dis[adj_node] = dis[min_node] +wt
            
            count -=1 
        
        return dis

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends