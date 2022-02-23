from collections import deque,defaultdict

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, vertices, adj):
        # Code here
        
        indegree = [0]*(vertices)
        graph = defaultdict(list)
        ququ = deque()
        ans = []
            
        for node in range(vertices):
            

            for adj_node in adj[node]:
                graph[node].append(adj_node)
            
                indegree[adj_node] +=1
        
        for node in range(vertices):
            if (indegree[node] == 0):
                ququ.append(node)
        
        # print(ququ)
        while(ququ):
            
            node = ququ.popleft()
            ans.append(node)
            
            for adj_node in graph[node]:
                
                indegree[adj_node] -=1
                if (indegree[adj_node] == 0):
                    ququ.append(adj_node)
            
        
        # print(ans)
        return ans
        


#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends