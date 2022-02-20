# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    
    
    def serialize(self, root):
        
        def solve(root):
            if (root is None):
                self.path += "#"
                return
            
            self.path+= str(root.val)+ "_"
            
            solve(root.left)
            solve(root.right)
        
        self.path = ""
        solve(root)
        # print(self.path)
        return self.path

    def deserialize(self, data):
        
        def solve(pos):
            if (pos[0] == size  ):
                return 
            
            if (data[pos[0]] =='#'):
                pos[0] +=1
                return None
            
            sign = 1
            if (data[pos[0]] == '-'):
                
                pos[0] +=1
                sign = -1
            
            curr_num = 0
            while(pos[0] < size):
                
                if (data[pos[0]].isdigit()):
                    
                    curr_num = curr_num*10 + int(data[pos[0]])
                    pos[0] +=1
                
                else:
                    break
            
            pos[0] +=1
            
            root = TreeNode(curr_num*sign)
            
            root.left = solve(pos)
            root.right = solve(pos)
            
            return root
        
        size = len(data)
        root = solve([0])
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))