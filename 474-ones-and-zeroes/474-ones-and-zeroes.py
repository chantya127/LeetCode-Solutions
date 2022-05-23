class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def solve(strs , m , n ,pos):
            
            if pos<0 or m<0 or n<0:
                return 0
            
            key = str(m)+ '_' + str(n) + '_' + str(pos)
            
            if key in dd.keys():
                return dd[key]
            
            zeros = strs[pos].count("0")
            ones = strs[pos].count("1")
            
            r1 = 0
            if m>=zeros and n>=ones:
                r1 = 1 + solve(strs , m-zeros,n-ones , pos-1)
            
            
            r2 = solve(strs , m , n ,pos-1)
            
            dd[key] = max(r1 , r2)
            return dd[key]
                    
        dd = {}
        return solve(strs , m , n, len(strs)-1)