#User function Template for python3

from math import log

class Solution:
    def height(self, n):
        # code here
        
        if (n == 1):
            return n
        
        level = 0
        curr_sum = 0
        while(curr_sum <= n):
            
            curr_sum += level+1
            
            level +=1
            
        return level-1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.height(N))
# } Driver Code Ends