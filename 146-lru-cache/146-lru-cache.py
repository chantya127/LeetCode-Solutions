class Node:
    def __init__(self , key = -1 , val = -1):
        
        self.prev  = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        
        self.head = Node()
        
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.cache = {}
        
        self.capacity = capacity
        
    
    def remove(self , node):
        
        #print(node)
        prev_node = node.prev
        
        next_node = node.next
        
        #print(node.key , node.val , prev_node , next_node)
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def add(self , node):
        
        last_node = self.tail.prev
        
        last_node.next = node
        node.prev = last_node
        
        #print(self.tail.prev.key , 'sss' , self.head)
        
        node.next = self.tail
        self.tail.prev = node
        
        
    
    def get(self, key: int) -> int:
        
        if (key in self.cache):
            
            node = self.cache[key]
            
            #print(node , 'ffff')
            self.remove(node)
            
            self.add(node)
            
            return node.val
    
        else:
            return -1
            
        

    def put(self, key: int, value: int) -> None:
        
        if (key in self.cache):
            
            node = self.cache[key]
            
            node.val = value
            self.cache[key] = node
            
            
            #print('zzz' , node)
            self.remove(node)
            
            self.add(node)
            return
        
        else:
            
            new_node = Node(key,value)
            
            self.cache[key] = new_node
            self.add(new_node)
            
            if (len(self.cache) > self.capacity):
                
                least_freq_node = self.head.next
                
                
                self.remove(least_freq_node)
                
                key = least_freq_node.key
                self.cache.pop(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)