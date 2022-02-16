# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            
            if (root is None):
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            
            both_ends = left + right
            if (ans[0] < both_ends):
                ans[0] = both_ends
            
            return 1 + max(left ,right)
        
        ans = [0]
        val = solve(root)
        
        return ans[0]
        