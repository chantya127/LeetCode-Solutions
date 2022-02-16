class node:
    
    def __init__(self):
        
        self.child = {}
        self.count = 0
        self.str = 0

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        
        def insert(root ,word):
            
            for ch in word:
                
                if (ch not in root.child):
                    
                    root.child[ch] = node()
                
                root = root.child[ch]
                root.count += 1
            
                
        def query(root , word):
            
            res = ''
            for ch in word:
                
                if (ch in root.child and root.child[ch].count == n):
                    res += ch
                    root = root.child[ch]
                
                else:
                    break
            
            return (res)
                
            
        n = len(s)
        if (n ==1):
            return s[0]
        
        ans = ""
        l = 0
        root = node()
        insert(root , s[0])
        
        for i in range(1,n):
            
            word = s[i]
            insert(root,  word)
        
        
        ans = query(root , s[0])
        
        return (ans)