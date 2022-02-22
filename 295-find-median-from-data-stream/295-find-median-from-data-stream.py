from heapq import heappush as push , heappop as pop

class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []
        

    def addNum(self, num: int) -> None:
        
        if (len(self.maxi) == 0 or abs(self.maxi[0]) > num):
            push(self.maxi, -num)
        
        else:
            push(self.mini , num)
        
        if (len(self.maxi)+1 > len(self.mini)):
            ele = pop(self.maxi)
            push(self.mini , -ele)
        
        if(len(self.mini) > len(self.maxi)):
            ele = pop(self.mini)
            push(self.maxi , -ele)
            
        

    def findMedian(self) -> float:
        
        if (len(self.maxi) + len(self.mini))%2 ==0:
            
            low = -self.maxi[0]
            high = self.mini[0]
            
            # print((low + high)//2)
            return (low+high)/2
        
        else:
            return -self.maxi[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()