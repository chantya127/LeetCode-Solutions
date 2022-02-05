# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def  get_mid(root):
            
            if (root is None or root.next is None):
                
                return root
                
            slow , fast = root,root
            
            while(fast.next and fast.next.next):
                
                slow = slow.next
                fast = fast.next.next
            
            return (slow)
        
        def get_rev(root):
            
            prev = None
            
            curr = root
            nexa = root
            while(nexa):
                
                nexa = nexa.next
                curr.next = prev
                
                prev = curr
                curr = nexa
            
            return(prev)
        
        
        # 1 -> 2 -> 2 ->1
        
        mid = get_mid(head)
        
        root = mid.next
        mid.next = None
        
        root = get_rev(root)
        
        temp = root
#         while(temp):
#             print(temp.val , end ="->")
#             temp = temp.next
        
#         print()
        
        while(head and root):
            
            # print(root.val , head.val ,mid.val)
            if (head.val != root.val):
                return (False)
            
            head = head.next
            root = root.next
        
        return (True)
        
        