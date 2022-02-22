"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def solve(root , org_node , vis):
            
            vis[root.val] = root
            
            for adj in org_node.neighbors:
                
                if (adj.val not in vis):
                    new_node = Node(adj.val)
                    root.neighbors.append(new_node)
                    solve(new_node , adj , vis)
                
                else:
                    new_node = vis[adj.val]
                    root.neighbors.append(new_node)
        
        if (node is None):
            return None
        
        vis = {}
        
        dup_root = Node(node.val)
        vis[dup_root.val] = dup_root
        
        for adj in node.neighbors:
            
            if (adj.val not in vis):
                
                new_node = Node(adj.val)
                dup_root.neighbors.append(new_node)
                solve(new_node , adj , vis)
            
            else:
                new_node = vis[adj.val]
                dup_root.neighbors.append(new_node)
        
        return dup_root