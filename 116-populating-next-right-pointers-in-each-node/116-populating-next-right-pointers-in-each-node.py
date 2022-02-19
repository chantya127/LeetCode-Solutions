"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        level = root
        
        while(level):
            
            curr = level
            
            while(curr):
                
                if (curr.left):
                    curr.left.next = curr.right
                
                if (curr.right and curr.next and curr.next.left):
                    curr.right.next = curr.next.left
                
                curr =curr.next
            
            level = level.left
        
        return root
        