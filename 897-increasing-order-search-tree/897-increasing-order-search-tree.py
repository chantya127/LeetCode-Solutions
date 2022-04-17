# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def solve(root , mhead , mtail):
            
            if (root is None):
                return
            
            
            solve(root.left , mhead , mtail)
            right = root.right
            
            root.left = None
            root.right = None
            
            mtail[0].right = root
            # print(root.val , mtail[0].val , mhead[0].val)
            mtail[0] = mtail[0].right
            
            solve(right , mhead , mtail)
        
        
        mhead = [TreeNode(-1)]
        mtail = [TreeNode(-1)]
        mhead[0].right = mtail[0]
        
        # print(mtail)
        
        solve(root, mhead , mtail)
        
        return (mhead[0].right.right)