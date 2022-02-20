# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def solve(root , pos):
            
            if (root is None or pos[0] > k):
                return 
            
            solve(root.left , pos)
            
            if (pos[0] == k-1):
                ans[0] =  root.val
                
            pos[0] +=1
            solve(root.right , pos)
            
        ans = [float('inf')]
        solve(root , [0])
        
        return ans[0]