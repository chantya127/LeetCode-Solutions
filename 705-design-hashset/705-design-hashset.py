class node:
    
    def __init__(self ,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.maxi = 4000
        self.arr = [None for _ in range(self.maxi)]
        
    
    def get_hash(self, key):
        
        return ( (key+7) % self.maxi)
    
    def add(self, key: int) -> None:
        
        idx = self.get_hash(key)
        temp = node(key)
        
        if (self.arr[idx] == None):
            self.arr[idx] = temp
        
        else:
            head = self.arr[idx]
            prev = None
            while(head):
                
                if (head.key == key):
                    return
                prev = head
                head = head.next
            
            prev.next = temp
        

    def remove(self, key: int) -> None:
        
        idx = self.get_hash(key)
        
        if (self.arr[idx] == None):
            return
        
        else:
            head = self.arr[idx]
            
            if (head.key == key):
                
                self.arr[idx] = head.next
                return 
                
            prev = head
            head = head.next
            while(head):
                
                if (head.key == key):
                    prev.next = head.next
                prev = head
                head = head.next
                    

    def contains(self, key: int) -> bool:
        
        """
        Returns true if this set contains the specified element
        """
        idx = self.get_hash(key)
        
        if (self.arr[idx] == None):
            
            False
        
        head = self.arr[idx]
        while(head):

            if (head.key == key):
                return True
            head = head.next

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)