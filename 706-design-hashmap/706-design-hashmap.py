class node:
    
    def __init__(self,key , data):
        self.data = data
        self.key = key
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.maxi = 1500
        self.arr  = [None for _ in range(self.maxi)]
        
        
    def get_hash(self , key):
        
        return key % self.maxi
    
    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        
        idx = self.get_hash(key)
        
        if (self.arr[idx] == None):
            self.arr[idx] = node(key , val)
        
        else:
            
            head = self.arr[idx]
            if (head.key == key):
                head.data = val
                return 
            
            prev = head
            head = head.next
            while(head):
                
                if (head.key == key):
                    head.data = val
                    return
                
                prev = head
                head = head.next
            
            prev.next = node(key ,val)
            

    def get(self, key: int) -> int:
        
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        idx = self.get_hash(key)
        if (self.arr[idx] == None):
            return -1
        
        head = self.arr[idx]
        while(head):
            
            k,v = head.key , head.data
            if (k == key):
                return v
            
            head = head.next
        
        return -1
            
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        idx = self.get_hash(key)
        if (self.arr[idx] == None):
            return
        
        head = self.arr[idx]
        if (head.key == key):
            self.arr[idx] = head.next
            return 
        
        else:
            
            prev = head
            head = head.next
            while(head):
                
                if (head.key == key):
                    prev.next = head.next
                    break
                
                prev = head
                head = head.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)