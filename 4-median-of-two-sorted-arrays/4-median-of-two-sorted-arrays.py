class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        
        if len(arr1) > len(arr2):
            holder1 = arr1 
            holder2 = arr2
            
            arr1 = holder2
            arr2 = holder1
        n1 = len(arr1)
        n2 = len(arr2)
        low = 0
        high =  n1
        count = 0
        while low<=high:
            part1 = (low + high)//2
            part2 = (n1+ n2)//2 - part1
            
            if part1>0:
                l1 = arr1[part1-1]
            else:
                l1 = float('-inf')
                
            if part2>0:
                l2 = arr2[part2-1]
            else:
                l2 = float('-inf')
                
            if part1 == n1:
                r1 = float('inf')
            else:
                r1 = arr1[part1]
            
            if part2 == n2:
                r2 = float('inf')
            else:
                r2 = arr2[part2]
                
            if l2 > r1:
                low = part1 +1
                
            elif l1 > r2:
                high = part1 -1
            else:
                if (n1+n2)%2 == 0:
                    
                    return (max(l1,l2) + min(r1,r2))/2
                
                else:
                    return min(r1,r2)
        return 2