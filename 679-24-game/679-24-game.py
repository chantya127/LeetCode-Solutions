class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def find(cards):
            if (len(cards) == 1):
                return abs(cards[0] - 24.0) <= 0.1
            
            for i in range(1,len(cards)):
                for j in range(i):

                    nexa = cards[:]

                    a,b = cards[i] , cards[j]
                    
                    nexa.pop(i)
                    nexa.pop(j)

                    vals = [a+b , a*b , a-b,b-a]
                    if (b > 0):
                        vals.append(a/b)
                    
                    if (a > 0):
                        vals.append(b/a)
                    
                    for v in vals:

                        nexa.append(v)
                        if (find(nexa)):
                            return True
                        
                        nexa.pop()
            
            return False


        return find(nums)