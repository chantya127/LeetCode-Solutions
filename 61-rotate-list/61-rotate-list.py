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
        
        if (head is None or head.next is None):
            return head
        
        size = get_size(head)
        
        k = k%size
        if (k == 0):
            return head
        
        tail = head
        sec = head
        prev = None
        
        for _ in range(k-1):
            
            tail = tail.next
        
        
        while(tail and tail.next):
            prev = sec
            sec = sec.next
            
            tail = tail.next
        
        # print(sec.val)
        if (prev):
            prev.next = None
            tail.next = head
            
        return (sec)
        
        