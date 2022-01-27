#User function Template for python3



class Solution:
    def find3number(self,arr, size):
        # code here
        
        
        left_small = [-1]*(size)
        right_big = [-1]*(size)
        
        prev = arr[0]
        
        for idx in range(1,size-1,1):
            
            curr = arr[idx]
            if (curr > prev):
                left_small[idx] = prev
            
            prev = min(prev ,curr)
        
        prev = arr[-1]
        for idx in range(size-2,0,-1):
            curr = arr[idx]
            if (curr < prev):
                right_big[idx] = prev
            
            prev = max(prev  ,curr)
        
        for idx in range(1,size-1,1):
            if (left_small[idx] != -1 and right_big[idx] != -1):
                return [left_small[idx] , arr[idx] , right_big[idx]]
        
        return []
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, lis, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis)!=0 and len(lis)!=3:
        print(-1)
        continue
    if len(lis)==0:
        print(0)
    elif lis[0]<lis[1] and lis[1]<lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)
        
# } Driver Code Ends