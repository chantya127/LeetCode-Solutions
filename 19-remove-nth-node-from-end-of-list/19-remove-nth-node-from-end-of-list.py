# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = None
        
        temp = head
        
        for _ in range(n-1):
            
            temp = temp.next
        
        prev = None
        curr = head
        while(temp and temp.next):
            prev = curr
            curr = curr.next
            temp = temp.next
        
        if (prev):
            prev.next = curr.next
        
        else:
            head = head.next
        return head
            