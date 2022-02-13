class node:
    
    def __init__(self):
        self.child = {}
        self.end = 0

class Trie:

    def __init__(self):
        
        self.root = node()
        
    def insert(self, word: str) -> None:
        
        temp = self.root
        
        for ch in word:
            
            idx = ord(ch) - ord('a')
            if (ch not in temp.child):
                temp.child[ch] = node()
            
            temp = temp.child[ch]
        
        temp.end = 1
        

    def search(self, word: str) -> bool:
        
        temp = self.root
        
        for ch in word:
            
            if (ch not in temp.child):
                return False
            
            temp = temp.child[ch]
        
        return temp.end == 1

    def startsWith(self, prefix: str) -> bool:
        
        temp = self.root
        
        for ch in prefix:
            
            if (ch not in temp.child):
                return False
            
            temp = temp.child[ch]
        
        return True
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)