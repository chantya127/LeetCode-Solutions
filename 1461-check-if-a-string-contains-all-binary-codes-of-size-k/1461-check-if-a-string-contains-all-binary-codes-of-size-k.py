class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seti = set()
        if s == 0:
            return True
        
        limit = 2**k
        for i in range(len(s)-k+1):
            curr = s[i:i+k]
            if curr not in seti:
                seti.add(curr)
                limit-=1
            if limit ==0:
                return True
        return False   