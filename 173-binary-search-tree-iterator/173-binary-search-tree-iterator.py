# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.stack = deque()
        temp = root
        while(temp):
            self.stack.append(temp)
            temp = temp.left
        
    def next(self) -> int:
        
        node = self.stack.pop()
        val = node.val
        
        temp = node.right
        while(temp):
            
            self.stack.append(temp)
            temp = temp.left
        
        return val
        

    def hasNext(self) -> bool:
        
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

    
    # 7
    # 3