# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        def dfs(node):
            if not node: return False
            if node == target: return True
            L, R = dfs(node.left), dfs(node.right)
            if L or R: self.path += [0] if L else [1]
            return L or R
        
        self.path = []
        dfs(original)
        for i in self.path[::-1]:
            cloned = cloned.left if i == 0 else cloned.right
        
        return cloned
        