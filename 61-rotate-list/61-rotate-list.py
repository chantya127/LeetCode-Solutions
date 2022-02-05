# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def get_size(root):
            
            count = 0
            
            while(root):
                count +=1
                root = root.next
            
            return (count)
        
        def get_rev(root):
            
            prev = None
            curr  = root
            nexa = root
            
            while(nexa):
                
                nexa = nexa.next
                curr.next = prev
                
                prev = curr
                curr = nexa
            
            return (prev)
        
        if (head is None or head.next is None):
            return head
        
        size = get_size(head)
        
        k = k%size
        if (k == 0):
            return head
        
        fir = head
        sec = head
        prev = None
        tail = None
        
        for _ in range(k-1):
            
            tail = fir
            fir = fir.next
        
        
        # print(sec.val)
        while(fir and fir.next):
            prev = sec
            sec = sec.next
            
            tail = fir
            fir = fir.next
        
        # print(sec.val)
        if (prev):
            prev.next = None
            fir.next = head
            
        return (sec)
        
        