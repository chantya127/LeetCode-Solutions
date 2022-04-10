class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        summe =0 
        for val in ops:
            if (val.isdigit() or val[0] == "-"):
                val = int(val)
                stack.append(val)
                summe += val
            
            elif (val == "D"):
                
                prev = stack[-1]
                stack.append(prev*2)
                summe += prev*2
            
            elif(val == "C"):
                prev = stack.pop()
                summe -= prev
                
            else:
                # print(val)
                last,sec_last= stack[-1] , stack[-2]
                stack.append(last + sec_last)
                summe += last + sec_last
            
            # if (len(stack) >2):
            #     stack.pop(0)
        
        return (summe)
        