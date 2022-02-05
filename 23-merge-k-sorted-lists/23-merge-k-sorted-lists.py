from heapq import heappush as push , heappop as pop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def solve(lists , pos , n):
            
            n = len(lists) 
            mhead = mtail = ListNode(-1)
            heap = []
            
            for i in range(n):
                if lists[i]:
                    push(heap , (lists[i].val ,i , lists[i]))
            
            while(heap):
                
                val , _, node = pop(heap)
                mtail.next = node
                mtail = mtail.next
                if (node.next):
                    i+=1
                    push(heap , (node.next.val, i , node.next))
                
                mtail.next = None
            
            return mhead.next
                
            
        
        if len(lists) == 0:
            return None
        
        return solve(lists, 0 , len(lists))