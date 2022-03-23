# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], lo: int, hi: int) -> Optional[TreeNode]:
        
        def find(root):

            if (root is None):
                return None
            
            root.left  = find(root.left)
            root.right = find(root.right)

            if (lo <= root.val <= hi):
                return root
            
            if (root.left): return root.left

            return root.right

        return find(root)