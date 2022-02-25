#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation

    def bellman_ford(self, v, adj, s):
        #code here
        
        dis = [100000000]*(v)
        
        dis[s] = 0
        
        for i in range(v):
            
            for (u,v,w) in adj:
                dis[v] = min(dis[v] , dis[u] + w)
                
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
        adj = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends