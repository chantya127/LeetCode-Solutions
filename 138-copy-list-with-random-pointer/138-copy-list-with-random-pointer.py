"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if (head is None):
            return head
        
        temp = head
        
        while(temp):
            
            next_node = temp.next
            
            new_node = Node(temp.val)
            
            temp.next = new_node
            new_node.next = next_node
            
            temp = next_node
        
        temp = head
        while(temp):
            
            if (temp.random):
                temp.next.random = temp.random.next
            
            temp = temp.next.next
        
        org_head = head
        dup_head = head.next
        temp = head
        
        while(temp and temp.next):
            
            nexa = temp.next
            
            temp.next = temp.next.next
            
            temp = nexa
        
        return (dup_head)
            
            
            