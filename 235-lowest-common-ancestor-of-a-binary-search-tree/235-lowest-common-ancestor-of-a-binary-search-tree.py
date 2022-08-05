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
            
            if (root == p or root == q):
                return root
            
            left = solve(root.left)
            right = solve(root.right)
            
            if (left and right):
                return (root)
            
            if (left):
                return left
            
            return right
            
        
        ans = solve(root)
        return ans