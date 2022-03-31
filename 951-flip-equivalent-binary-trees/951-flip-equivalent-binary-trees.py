# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def solve(r1 , r2):
            
            if (r1 is None and r2 is None):
                return True
            
            if (r1 is None or r2 is None):
                return False
            
            v1 = False
            
            if (r1.val == r2.val):
                v1 = solve(r1.left , r2.left) and solve(r1.right , r2.right)
                
                if (v1):
                    return True
                
                v1 = solve(r1.left , r2.right) and solve(r1.right , r2.left)
                
            return v1
        
        ans = solve(root1 , root2)
        return ans