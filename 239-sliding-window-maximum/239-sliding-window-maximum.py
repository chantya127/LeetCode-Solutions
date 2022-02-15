class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        from collections import deque
        
        ququ = deque()
        n = len(arr)
        
        if n<k:
            return 0
        
        res = []
        for i in range(k):
            while (len(ququ)) and arr[i] > arr[ququ[-1]]:
                ququ.pop()
            ququ.append(i)
        
        for i in range(k,n):
            
            res.append(arr[ququ[0]])

            while len(ququ) and arr[i] >= arr[ququ[-1]]:
                ququ.pop()
                
            while len(ququ) and i - ququ[0] >=k:
                ququ.popleft()
                
            ququ.append(i)    
            
        res.append(arr[ququ[0]])
        return res