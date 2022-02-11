#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		if (m == 1):
		    return 1
		   
		ans = 1
		x = 2
		while(pow(x,n) <= m):
		    if (pow(x,n) == m):
		        return x
		    x +=1
		
		return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends