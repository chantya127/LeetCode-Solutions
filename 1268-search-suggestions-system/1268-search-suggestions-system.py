class trie:
    
    def __init__(self):
        
        self.child ={}
        self.words = []
        self.end = 0
    

class Solution:
    
    
    def insert(self , word , root):
        
        for ch in word:
            
            index = ord(ch) - ord('a')
            if index not in root.child:
                root.child[index] = trie()
            
            root = root.child[index]
            if len(root.words)<3:
                root.words.append(word)
                
        root.end = 1        
        
    
    def query(self , root , target):
        
        ptr = 0
        ans = [[]]*(len(target))
        for ch in target:
            
            index = ord(ch) - ord('a')
            if index in root.child:
                root = root.child[index]
                ans[ptr] = root.words
                ptr+=1
            else:
                break
        return  ans  
        
    
    def suggestedProducts(self, products: List[str], target: str) -> List[List[str]]:
        
        
        products.sort()
        root = trie()
        for word in products:
            self.insert(word , root)
        
        return self.query(root, target)
        
         
        
        
        