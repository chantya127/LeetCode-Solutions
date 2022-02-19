# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def solve(root):
            
            if (root is None):
                
                return root
            
            if (root.val == target):
                return (root)
            
            elif(root.val > target):
                
                return solve(root.left)
        
            else:
                return solve(root.right)
        
        ans = solve(root)
        
        return ans