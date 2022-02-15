#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,size):
        
        left_bound = [0]*(size)
        right_bound = [0]*(size)
        
        final_arr = [0]*(size)
        
        stack = []
        
        for idx in range(size):
            
            curr = arr[idx]
            
            while(stack and arr[stack[-1]] >= curr):
                stack.pop()
            
            if (len(stack) == 0):
                left_bound[idx] = -1
            
            else:
                left_bound[idx] = stack[-1]
                
            stack.append(idx)
        
        stack = []
        for idx in range(size-1,-1,-1):
            
            curr = arr[idx]
            while(stack and arr[stack[-1]] >= curr):
                stack.pop()
                
            if len(stack) == 0:
                right_bound[idx] = size
            
            else:
                
                right_bound[idx] = stack[-1]
            
            stack.append(idx)
                
                
        for idx in range(size):
            
            spread = right_bound[idx] - left_bound[idx] -1
            
            final_arr[spread-1] = max(final_arr[spread-1] , arr[idx])
            
            # print(spread , arr[idx])
        
        for idx in range(size-2,-1,-1):
            final_arr[idx] = max(final_arr[idx] , final_arr[idx+1])
            
        return (final_arr)
        
    # code here
    # [10,20,30]
    
    # 10 -> 3
    # 20 -> 2
    # 30 -> 1
    
    # [30,20,10]
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.maxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

# } Driver Code Ends