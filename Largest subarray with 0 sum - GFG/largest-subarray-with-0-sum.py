#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, size, arr):
        #Code here
        
        indices = {0:-1}
        summe = 0
        ans = 0
        for idx in range(size):
            curr = arr[idx]
            summe += curr
            if (summe in indices):
                
                length = idx - indices[summe]
                ans = max(ans ,length)
            
            else:
                indices[summe] = idx
        
        return (ans)
        

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends