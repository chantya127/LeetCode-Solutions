#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        def find_prev_meet(idx):
            
            low = 0
            high = idx-1
            
            stime = meetings[idx][0]
            
            while(low <= high):
                
                mid = (high-low)//2 + low
                
                if (meetings[mid][1] < stime):
                    
                    if (mid+1 < n and meetings[mid+1][1] < stime):
                        low = mid+1
                    
                    else:
                        return mid
                
                else:
                    high = mid-1
            
            return -1
        
        meetings = [[start[i] , end[i]] for i in range(n)]
        
        meetings.sort(key = lambda x : x[1])
        
        dp = [0]*(n)
        dp[0] = 1
        
        for idx in range(1, n,1):
            
            inc = 1
            
            prev = find_prev_meet(idx)
            if(prev != -1):
                inc += dp[prev]
            
            dp[idx] = max(dp[idx-1] , inc)

        return (dp[-1])        

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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends