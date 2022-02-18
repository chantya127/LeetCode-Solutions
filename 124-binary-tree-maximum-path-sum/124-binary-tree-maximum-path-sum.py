# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            
            if (root is None):
                return float('-inf')
            
            
            left = solve(root.left)
            right = solve(root.right)
            
            both_inc = root.val + left + right
            
            one_inc = root.val + max(left , right)
            
            only_root = root.val
            
            maxi = max(only_root , both_inc , one_inc)
            
            if (maxi > ans[0]):
                ans[0] = maxi
            
            return max(only_root , one_inc)
            
        
        ans = [float('-inf')]
        
        val = solve(root)
        
        return ans[0]