# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#         1
#      2       3
#    4   5    6  7
#   8 9 10 1

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        ququ = deque()
        
        ququ.append((root,1))
        
        while(ququ):
            
            first,last = ququ[0][1], ququ[-1][1]
            
            dis = last-first+1
            ans = max(ans , dis)
            size = len(ququ)
            
            for idx  in range(size):
                
                node,dis = ququ.popleft()
                
                if (node.left):
                    ququ.append((node.left , dis*2))
                
                if (node.right):
                    ququ.append((node.right , dis*2+1))
        
        return (ans)