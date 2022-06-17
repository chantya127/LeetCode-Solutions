# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 0 -> has , 1 -> covered , 2 -> need

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            
            if (root is None):
                
                return scene[1]
            
            left = solve(root.left)
            right = solve(root.right)
            
            if (left == 2 or right == 2):
                
                self.cam +=1
                return (0)
            
            elif (left == 0 or right ==0):
                return 1
        
            return 2
        
        self.cam = 0
        scene = [0,1,2]
        
        ans = solve(root)
        if (ans ==2):
            self.cam +=1
        
        return self.cam
        