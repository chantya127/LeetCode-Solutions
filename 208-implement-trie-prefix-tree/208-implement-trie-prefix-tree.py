class Node:
    
    def __init__(self):
        self.end = 0
        self.child = {}


class Trie:

    def __init__(self):
        
        self.root = Node()
        

    def insert(self, word: str) -> None:
        
        root = self.root
        for ch in word:
            if (ch not in root.child):
                root.child[ch] = Node()
                
            root = root.child[ch]
        
        root.end = 1
        

    def search(self, word: str) -> bool:
        
        root = self.root
        for ch in word:
            if (ch not in root.child):
                return False
            
            root = root.child[ch]
            
        return (root.end == 1)

    def startsWith(self, prefix: str) -> bool:
        
        root = self.root
        
        for ch in prefix:
            if(ch not in root.child):
                return False
            root = root.child[ch]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)