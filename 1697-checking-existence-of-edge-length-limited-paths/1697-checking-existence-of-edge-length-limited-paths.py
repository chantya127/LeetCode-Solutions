class disjoint_set:
    
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find_parent(self,x):
        if (self.parent[x] == x):
            return x
        
        self.parent[x] = self.find_parent(self.parent[x])
        
        return self.parent[x]
    
    def union(self,u,v):
        
        p1 = self.find_parent(u)
        p2 = self.find_parent(v)
        
        if(p1 != p2):
            
            if (self.rank[p1] < self.rank[p2]):
                self.parent[p1] = p2
            
            elif (self.rank[p2] < self.parent[p1]):
                self.parent[p2] = p1
            
            else:
                self.parent[p2] = p1
                self.rank[p1] +=1
        
    def is_connected(self,u,v):
        
        p1 = self.find_parent(u)
        p2 = self.find_parent(v)
        
        #print(u,v, p1,p2)
        
        return (p1 == p2)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edge: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        edge_size = len(edge)
        queries_size = len(queries)
        ans= [False]*(queries_size)
        
        edge.sort(key = lambda x :x[2])
        
        new_queries = [[queries[idx][0],queries[idx][1],queries[idx][2],idx] for idx in range(queries_size)]
        
        new_queries.sort(key = lambda x : x[2])
        edge_ptr = 0
        
        dsu = disjoint_set(n)
        
        # print(edge)
        # print(new_queries)
        
        for ptr in range(queries_size):
            
            curr = new_queries[ptr]
            u,v,req_dis ,idx =  curr[0],curr[1],curr[2],curr[3]
            
            while(edge_ptr < edge_size and edge[edge_ptr][2] < req_dis):
                
                src,dest = edge[edge_ptr][0],edge[edge_ptr][1]
                
                dsu.union(src,dest)
                edge_ptr +=1
                
                #print(src,dest , req_dis)
            
            if (dsu.is_connected(u,v)):
                ans[idx] = True
            
        
        return ans