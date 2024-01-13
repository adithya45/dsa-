from queuesll import Queue
class BTNode:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
class btree:
    def __init__(self):
        self.root=None
    def insert(self,ele):
        newnode=BTNode(ele)
        if self.root==None:
            self.root=newnode
        else:
            q=Queue()
            q.enqueue(self.root)
            while True:
                temp=q.peek()
                if temp.lc==None:
                    temp.lc=newnode
                    return
                else:
                    q.enqueue(temp.lc)
                if temp.rc==None:
                    temp.rc=newnode
                    return
                else:
                    q.enqueue(temp.rc)
                q.dequeue()
    def inorderdisplay(self,r):
        if r!=None:
            self.inorderdisplay(r.lc)
            print(r.data)
            self.inorderdisplay(r.rc)
    def preorderdisplay(self,r):
        if r!=None:
            print(r.data)
            self.preorderdisplay(r.lc)
            self.preorderdisplay(r.rc) 
    def postorderdisplay(self,r):
        if r!=None:
            self.postorderdisplay(r.lc)
            self.postorderdisplay(r.rc)  
            print(r.data)           
    def height(self,r):
        if r==None:
            return 0
        else:
            l=self.height(r.lc)
            r=self.height(r.rc)
            return(max(l,r)+1)
    def search(self,key):
        if self.root==None:
            print("tree is empty")
        else:
            r=self.checkNode(self.root,key)
            if r:
                print("element  found")
            else:
                print("elemnt not found")
    def checkNode(self,cn,key):
        if(cn== None):
            return False
        elif(cn.data==key):
            return True
        else:
            res=self.checkNode(cn.lc,key)
            if res:
                return res
            res=self.checkNode(cn.rc,key)
            return res
    def delete(self):
        if not self.root:
            return

        q = Queue()
        q.enqueue(self.root)
        last_node = None
        parent_last_node = None

        while not q.is_empty():
            current = q.peek()
            q.dequeue()

            if current.lc:
                q.enqueue(current.lc)
                parent_last_node = current
            if current.rc:
                q.enqueue(current.rc)
                parent_last_node = current

            last_node = current

        if last_node and parent_last_node:
            if parent_last_node.lc == last_node:	
                parent_last_node.lc = None
            else:
                parent_last_node.rc = None
        else:
            self.root = None

obj=btree() 
print("Menu:\n1.Insert\n2.Delete\n3.InorderDisplay\n4.PreorderDisplay\n5.PostorderDisply\n6.Height")
while True:
    choice=int(input("enter your choice:"))
    if choice==1:
        val=input("enter the value")
        obj.insert(val)
    elif choice==2:
        obj.delete()
    elif choice==3:
        obj.inorderdisplay(obj.root)
    elif choice==4:
        obj.preorderdisplay(obj.root)
    elif choice==5:
        obj.postorderdisplay(obj.root)
    elif choice==6:
        h=obj.height(obj.root)
        print("height of tree:",h-1)
    else:
        break
'''
def levelOrderTraversal(root):
    result = []
    if not root:
        return result
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        current_node = queue.peek()
        result.append(current_node.value)
        queue.dequeue()
        if current_node.left:
            queue.enqueue(current_node.left)
        if current_node.right:
            queue.enqueue(current_node.right)

    return result
'''
                
                    