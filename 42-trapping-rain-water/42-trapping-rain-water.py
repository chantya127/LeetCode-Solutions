# maxl = 2,7
# maxr = 2,7

# ans = 3 + 2 +1




class Solution:
    def trap(self, height: List[int]) -> int:
        
        size = len(height)
        
        mleft , mright = 0,0
        
        low,high = 0,size-1
        
        ans = 0
        
        while(low < high):
            
            if (height[low] <= height[high]):
                
                if (height[low] >= mleft):
                    mleft = height[low]
                
                else:
                    ans += mleft-height[low]
                
                low +=1
            
            else:
                if(height[high] >= mright):
                    mright = height[high]
                
                else:
                    ans += mright - height[high]
                
                high -=1
                
        return (ans)