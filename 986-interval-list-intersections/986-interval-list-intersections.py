class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        
        p1,p2 = 0,0
        
        s1 , s2 = len(first) , len(second)
        
        ans = []
        
        while(p1 < s1 and p2 < s2):

            l1,l2 = first[p1][0] , second[p2][0]
            
            r1,r2 = first[p1][1] , second[p2][1]
            
            if (l1 <= l2 <= r1 or l2 <= l1 <= r2):
            
                left_bound = max(l1,l2)
                right_bound = min(r1,r2)

                ans.append([left_bound , right_bound])
            
            if (first[p1][1] < second[p2][1]):
                p1 +=1
            
            else:
                p2 +=1
            
#             while(p1 < s1 and p2 <s2 and first[p1][1] < second[p2][0]):
#                 p1 +=1
            
#             while(p2 <s2 and p1 < s1 and second[p2][1] < first[p1][0]):
#                 p2 +=1
        
        return ans