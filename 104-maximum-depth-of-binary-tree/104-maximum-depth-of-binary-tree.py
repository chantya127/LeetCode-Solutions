# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if (root is None):
            return 0
        
        ququ = deque()
        
        ans = 0
        
        level = 0
        
        ququ.append(root)
        
        while(ququ):
            size = len(ququ)
            
            for _ in range(size):
                
                node= ququ.popleft()
                if (node.left):
                    ququ.append(node.left)
                
                if (node.right):ququ.append(node.right)
            
            level +=1
        
        return level