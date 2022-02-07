#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        count = 0
        maxi = 0
        
        p1,p2 = 0,0
        
        while(p1 <n and p2 <n):
            
            if (arr[p1] <= dep[p2]):
                count +=1
                p1 +=1
            
            else:
                count -=1
                p2 +=1
            
            maxi = max(maxi , count)
        
        return (maxi)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends