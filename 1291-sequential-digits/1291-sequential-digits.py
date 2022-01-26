class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def solve(num , prev):

            if (low <= num <= high):
                ans.append(num)
            
            if (num > high or prev == 9):
                return
            
            add = prev+1
            solve(num*10 + add , add)

        ans = []
        num = 0
        start = 1
        for add in range(start , 10,1):
                
            curr_num= num*10 + add
            if (curr_num <= high):
                solve(curr_num , add)
                
        return sorted(ans)