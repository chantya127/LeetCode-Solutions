# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def solve(root):
            
            if (root is None):
                return None
            
            if(max(p.val ,q.val) < root.val):
                return solve(root.left)
            
            elif(min(p.val , q.val) > root.val):
                return solve(root.right)
            
            else:
                return root
        
        ans = solve(root)
        return ans