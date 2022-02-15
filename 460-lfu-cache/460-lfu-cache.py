
class Node:
    def __init__(self,key=-1, value=-1 , level =-1):
        
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
        self.level = level
        


class LFUCache:

    def __init__(self, capacity: int):
        
        self.level_cache = {}
        self.key_cache = {}
        
        self.capacity = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        
        if (key in self.key_cache):
            
            node = self.key_cache[key]
            
            node.level +=1
        
            self.remove_prev_level(node)
            
            self.insert_into_next_level(node.level , node,key)

            return node.value
        
        else:
            # print(self.key_cache , self.size)
            return -1
                

    def put(self, key: int, value: int) -> None:
        
        
        if (self.capacity == 0):
            return
        
        if (key not in self.key_cache):
            curr_level = 1
            self.size +=1
            node = Node(key,value,curr_level)
        
        else:
            
            node = self.key_cache[key]
            node.value = value            
            
            node.level +=1
            self.remove_prev_level(node)
            

        if(self.size > self.capacity) and (key not in self.key_cache):
            
            # find minimum level in level_cache
            
            min_level = float('inf')
            
            for level in self.level_cache:
                
                min_level = min(min_level , level)
            
            if min_level != float('inf'):
                
                self.size -=1
                head,tail = self.level_cache[min_level]

                if (head.next != tail and head.next != None):
                    
                    # remove least recently used node
                    
                    first_node = head.next
                    self.remove(first_node)

                    first_key = first_node.key
                    self.key_cache.pop(first_key)

                if (head.next == tail or head.next == None):
                    self.level_cache.pop(min_level)

        self.insert_into_next_level(node.level, node , key)
        
        
    
    def remove_prev_level(self,node):
        
        self.remove(node)
            
        prev_level = node.level-1

        if (prev_level in self.level_cache):
            prev_head , prev_tail = self.level_cache[prev_level]

            # no values left in prev level
            if(prev_head.next == prev_tail):
                self.level_cache.pop(prev_level)
        
    
    def insert_into_next_level(self,curr_level,node,key):
        
        if (curr_level not in self.level_cache):
            
            head = Node()
            tail = Node()

            head.next = tail
            tail.prev = head
            self.level_cache[curr_level] = [head,tail]
            
        else:
            head,tail = self.level_cache[curr_level]
            
        self.key_cache[key] = node
        self.insert(node, tail)
    
    def insert(self,new_node , tail):
        
        prev_node = tail.prev
        
        prev_node.next= new_node
        new_node.prev = prev_node
        
        new_node.next = tail
        tail.prev = new_node
    
    def remove(self,new_node):
        
        prev_node = new_node.prev
        next_node = new_node.next
        
        #print(new_node.key , new_node.value )
        
        prev_node.next = next_node
        next_node.prev = prev_node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# key = counter

# value => Linked list of same counter values