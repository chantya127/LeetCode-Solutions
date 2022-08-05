# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        if not root:
            return ans
        
        ququ = deque()
        ququ.append(root)
        
        while(ququ):
            size = len(ququ)
            curr = []
            for _ in range(size):
                node = ququ.popleft()
                curr.append(node.val)
                
                if (node.left):
                    ququ.append(node.left)
                
                if(node.right):
                    ququ.append(node.right)
            
            ans.append(curr)
        
        return (ans)