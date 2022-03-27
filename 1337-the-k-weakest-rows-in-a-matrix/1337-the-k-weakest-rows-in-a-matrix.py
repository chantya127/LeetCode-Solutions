class Solution:
    
    def solve(self , arr , n,m):
        
        low = 0
        high = m-1
        if arr[low] == arr[high] and arr[high] == 1:
            return m
        
        if arr[low] == arr[high] and arr[high] == 0:
            return 0
        
        while low<=high:
            mid = (low+high)//2
            if mid<n-1 and arr[mid]==1 and arr[mid+1] ==0:
                return mid +1
            if mid >0 and arr[mid-1] ==1 and arr[mid] == 0:
                return mid-1+1
            elif arr[mid] ==1:
                low = mid+1
            else:
                
                high = mid-1
                
        # print('hgigi')
        return m      
        
    
    def kWeakestRows(self, matrix: List[List[int]], k: int) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        dd = {i:0 for i in range(n)}
        for i in range(n):
            row = matrix[i]
            count = self.solve(row,n,m)
            dd[i] = count
            
        dd = dict(sorted(dd.items() , key = lambda it :it[1]))
        ans = []
        #print(dd)
        for key in dd.keys():
            if k==0:
                break
            ans.append(key)
            k-=1
        return ans    