# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def solve(root , pos):
            if (root is None):
                return
            
            solve(root.left , pos)
            
            pos[0] -=1
            if (pos[0] == 0):
                ans[0] = root.val
                return
            
            solve(root.right , pos)
            
        ans = [-1]
        solve(root , [k])
        return ans[0]