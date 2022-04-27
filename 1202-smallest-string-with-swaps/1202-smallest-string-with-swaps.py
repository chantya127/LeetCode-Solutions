class disjoint_set:
    
    def __init__(self,size):
        
        self.parent = [-1 for _ in range(size)]
    
    def find_parent(self , node):
        
        if (self.parent[node] == -1):
            return node
        
        self.parent[node] = self.find_parent(self.parent[node])
        return (self.parent[node])
    
    def add_edge(self , src,dest,s):
        p1 = self.find_parent(src)
        p2 = self.find_parent(dest)
        
        if (p1 != p2):
            
            v1 = ord(s[src]) -ord('a')
            v2 = ord(s[dest]) - ord('a')
            
            if (v1 <= v2):
                self.parent[p2] = p1
            
            else:
                self.parent[p1] = p2
        
        


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        size = len(s)
        obj = disjoint_set(size)
        
        for (u,v) in pairs:
            
            obj.add_edge(u,v,s)
        
        parent_to_char = defaultdict(list)
        for (u,v) in pairs:
            
            p1 = obj.find_parent(u)
            p2 = obj.find_parent(v)
            
            c1 = s[u]
            c2 = s[v]
            parent_to_char[p1].append([c1 , u])
            parent_to_char[p2].append([c2, v])
        
        # print(parent_to_char)
        ans = [ch for ch in s]
        vis = [0 for _ in range(size)]
        
        for key,val in parent_to_char.items():
            
            chars = []
            indices = []
            
            for (c,i) in val:
                if (vis[i] == 0):
                    chars.append(c)
                    indices.append(i)
                    vis[i] = 1
            
            chars.sort()
            indices.sort()
            # print(chars , indices , val)
            
            for i in range(len(indices)):
                ans[indices[i]] = chars[i]
        
        return (''.join(ans))
            
        
        
        
        