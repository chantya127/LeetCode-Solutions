class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def next_permuation(arr):
            
            def reverse(low , high):
                
                while(low < high):
                    
                    arr[low] , arr[high] = arr[high] , arr[low]
                    
                    low +=1
                    high -=1
            
            idx = -1
            
            for k in range(n-2,-1,-1):
                
                if(arr[k+1] > arr[k]):
                    idx = k
                    break
                    
            if(idx == -1):
                reverse( 0 , n-1)
            
            else:
                
                flag = -1
                for k in range(n-1,-1,-1):
                    if (arr[k] > arr[idx]):
                        flag = k
                        break
                
                arr[flag] , arr[idx] = arr[idx] , arr[flag]
                # print(arr,flag,idx)
                reverse(idx+1 ,n-1)
            
            
        
        num = [i for i in range(1,n+1)]
        
        for c in range(1,k):
            # print(num , c)
            next_permuation(num)
        
        # print(9*8*7*6*5*4*3*2)
#         num = [1,3,2]
        
#         next_permuation(num)
        return "".join(str(n) for n in num)