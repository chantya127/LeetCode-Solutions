#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        
        
        # arr2[] = {1, 4, 8, 10}
        # arr2[] = {2, 3, 6, 7, 9}
        
        # # 1,2,3,4,6,7,8,9,10   , 5 elements 2 are from 1 st array
        
        # low = 0 , high = 4
        
        # c1 = 2  -> l1 = 4 , r1 = 8 
        # c2 = 3     l2 = 6 , r2 = 7
        
        # low = 3,high = 4
        
        # c1 = 3 -> l1 = 
        
        def solve(a1,a2):
            
            s1,s2 = len(a1),len(a2)
            
            low = max(0,k-s2)
            high = min(k , s1)
            
            while(low <= high):
                
                c1 = (low+high)//2
                c2 = k-c1
                
                if(c1 >0):
                    l1 = a1[c1-1]
                
                else:
                    l1 = float('-inf')
                
                if (c2 >0):
                    l2 = a2[c2-1]
                
                else:
                    l2 = float('-inf')
                
                
                if (c1 <s1):
                    r1 = a1[c1]
                
                else:
                    r1 = float('inf')
                
                if (c2 < s2):
                    r2 = a2[c2]
                
                else:
                    r2 = float('inf')
                
                #print(l1,r2,l2,r1)
                if(l1 <= r2 and l2 <= r1):
                    return max(l1,l2)
                
                elif(l1 > r2):
                    high = c1-1
                
                else:
                    low = c1 +1
        
        
        if len(arr1)> len(arr2):
            val = solve(arr2, arr1)
        
        else:
            val = solve(arr1,arr2)
        
        return val
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends