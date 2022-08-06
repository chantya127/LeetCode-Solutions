
from heapq import heappush as push , heappop as pop

class MedianFinder:

    def __init__(self):
        
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        
        if (len(self.max_heap) == 0):
            push(self.max_heap , -num)
        
        elif(num < -self.max_heap[0]):
            push(self.max_heap , -num)
        
        else:
            push(self.min_heap , num)
        
        
        if (len(self.min_heap) > len(self.max_heap)):
            
            ele = pop(self.min_heap)
            push(self.max_heap , -ele)
            
            
        
        if (len(self.max_heap)  > len(self.min_heap)+ 1):
            
            ele = - pop(self.max_heap)
            push(self.min_heap , ele)
            
        
        # print(num , self.max_heap , self.min_heap)
        

    def findMedian(self) -> float:
        
        
        # print(self.max_heap , self.min_heap)
        
        ele_1 = - self.max_heap[0]
        
        if (len(self.min_heap) + len(self.max_heap))%2 == 0:
            
            ele_2 = self.min_heap[0]
            
            return (ele_1 + ele_2)/2
    
        else:
            return ele_1

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()