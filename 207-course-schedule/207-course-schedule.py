from collections import defaultdict

class Solution:
    def canFinish(self, courses: int, pre: List[List[int]]) -> bool:
        
        def is_cycle(node):
            
            # if (vis[node] == 2):
            #     print('kkk' , node)
            #     return True
            
            vis[node] = 2
            
            for adj in graph[node]:
                if (vis[adj] == 0):
                    if(is_cycle(adj)):
                        # print(adj , 'ccc')
                        return True
                
                elif(vis[adj] == 2):
                    # print(adj ,'dd')
                    return True
            
            vis[node] = 1
            return False
        
        graph = defaultdict(list)
        
        for (dest , src) in pre:
            graph[src].append(dest)
        
        vis = [0]*(courses)
        # print(graph)
        for node in graph.copy():
            if (vis[node] == 0):
                
                val = is_cycle(node)
                if (val):
                    return False
        
        return True