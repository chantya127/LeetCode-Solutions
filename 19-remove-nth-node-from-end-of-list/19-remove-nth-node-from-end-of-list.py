# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, root: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        # take 2 ptr approach
        # gap between 1 and 2 ptrs is n . 
        # Just maintain a prev node before the target node,and point prev.next =  target.next
        
        first = root
        sec = root
        prev = None
        
        for _ in range(1,n+1,1):
            
            first = first.next
        
        if (first is None):
            return(root.next)
        
        while(first):
            
            prev = sec
            sec = sec.next
            first = first.next
        
        prev.next = sec.next
        return (root)