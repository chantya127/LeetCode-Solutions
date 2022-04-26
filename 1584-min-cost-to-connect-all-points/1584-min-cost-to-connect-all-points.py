
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def get_dis(x1,y1 ,x2 , y2):
            
            return abs(x1-x2) + abs(y1 - y2)
        
        
        def find_parent(x):
            
            if (parent[x] == -1):
                return x
            
            parent[x] = find_parent(parent[x])
            return (parent[x])
        
        def add_edge(src , dest):
            
            p1 ,p2 = find_parent(src) , find_parent(dest)
            
            r1 = rank[p1]
            r2 = rank[p2]
            
            if (r1 < r2):
                parent[p1] = p2
            
            elif(r1 > r2):
                parent[p2] = p1
            
            else:
                parent[p2] = p1
                rank[p1] +=1
        
        def not_connected(src , dest):
            
            p1 = find_parent(src)
            p2 = find_parent(dest)
            # print(src , dest , p1,p2)
            
            return (p1 != p2 or (p1 == -1 or p2 == -1))
        
        edges = []
        
        size = len(points)
        
        for idx in range(size-1):
            for ptr in range(idx+1 , size,1):
                
                x1,y1 = points[idx][0] , points[idx][1]
                
                x2,y2 = points[ptr][0] , points[ptr][1]
                
                dis = get_dis(x1,y1 , x2, y2)
                
                edges.append([dis , idx , ptr])
        
        # print(edges)
        
        edges.sort(key = lambda it:it[0])
        
        parent = [-1 for _ in range(size)]
        rank = [1 for _ in range(size)]
        
        total_cost = 0
        edge_ptr , total_edges = 0 , 0
        while(edge_ptr < len(edges) and total_edges <size):
            
            cost  , src,dest = edges[edge_ptr][0], edges[edge_ptr][1] ,edges[edge_ptr][2]
            # print(cost , src , dest)
            if (not_connected(src , dest)):
                
                add_edge(src , dest)
                total_cost += cost
                
                # print(cost , src,dest)
                
                total_edges +=1
            
            edge_ptr +=1
        
#         print(edges)
#         print(total_edges , edge_ptr , size)
        return (total_cost)
        
                