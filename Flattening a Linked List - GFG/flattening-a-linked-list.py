#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    if (root is None or root.next is None):
        return root
    
    def solve(root):
        
        if (root.next is None):
            return root
        
        first = root
        sec = solve(root.next)
        
        new_root = Node(-1)
        tail = new_root
        
        while(first or sec):
            
            v1,v2 = float('inf') , float('inf')
            
            if (first):
                v1 = first.data
            
            if (sec):
                v2 = sec.data
            
            if(v1 < v2):
                tail.bottom = Node(v1)
                first = first.bottom
            
            else:
                tail.bottom = Node(v2)
                sec = sec.bottom
            
            tail = tail.bottom
        
        return (new_root.bottom)
        
    
    return solve(root)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends