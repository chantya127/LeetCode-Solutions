from collections import defaultdict , deque

class Solution:
    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:
        
        if (end not in words or  not end or not begin):
            return 0
        
        allcombo = defaultdict(list)
        size = len(begin)
        for w in words:
            for i in range(size):
                
                pattern = w[:i] +"_" + w[i+1:]
                allcombo[pattern].append(w)
        
        ququ = deque()
        ququ.append((begin, 1))
        vis= set()
        vis.add(begin)
        
        while(ququ):
            
            word , dis = ququ.popleft()
            for i in range(size):
                
                pat = word[:i] + "_" + word[i+1:]
                for string in allcombo[pat]:
                    if (string) == end:
                        return dis+1
                    
                    if (string not in vis):
                        vis.add(string)
                        ququ.append((string ,dis+1))
        
        return 0