# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def get_mid(root):
            
            slow = root
            fast = root
            
            
            while(fast and fast.next and fast.next.next):
                
                slow = slow.next
                fast = fast.next.next
            
            return (slow)
        
        def reverse(node):
            
            curr = node
            nexa = node
            prev = None
            
            while(nexa):
                nexa = nexa.next
                
                curr.next = prev
                prev = curr
                curr = nexa
            
            return (prev)
                
        
        mhead = ListNode(-1)
        mtail =mhead
        
        mid = get_mid(head)
        next_mid = reverse(mid.next)
        
        mid.next = None
        
        temp = head
        
        while(temp or next_mid):
            if (temp):
                mtail.next = temp
                temp = temp.next
                mtail = mtail.next
                
            if (next_mid):
                
                mtail.next = next_mid
                next_mid = next_mid.next
                mtail = mtail.next
                
            mtail.next = None 
        
        head = mhead.next
            
    