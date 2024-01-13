from queuesll import *

class Btnode:
    def __init__(self,data):
        self.data= data
        self.lc=self.rc=None
class BTree:
    def __init__(self):
        self.root= None
    def insert(self,ele):
        newnode = Btnode(ele)
        if self.root == None:
            self.root = newnode
        else:
            q = Queue()
            q.enqueue(self.root)
            while True:
                temp = q.peek()
                if temp.lc == None:
                    temp.lc =  newnode
                    return
                else:
                    q.enqueue()
                if temp.rc ==None:
                    temp.rc = newnode
                    return
                else:
                    q.enqueue()
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
            self.preorderdisplay(r.lc)
    def postroderdisplay(self,r):
        if r!=None:
            self.postroderdisplay(r.lc)
            self.postroderdisplay(r.rc)
            print(r.data)
    def height(self,r):
        if r==None:
            return 0
        else:
            ls=self.height(r.lc)
            rs=self.height(r.rc)
            return (max(ls,rs)+1)
    def search (self,key):
        if self.root==None:
            print("tree is empty")
        else:
            r = self.checknode(self.root,key)
            if r:
                print("ele found")
            else:
                print("nope")
    def checknode(self,cn,key):
        if cn==None:
            return False
        elif cn.data == key:
            return True
        else:
            res = self.checknode(cn.lc,key)
            if res:
                return res
            res = self.checknode(cn.rc,key)
            return res      
    def delete(self,key):
        if self.root==None:
            print ("Tree is Empty")
        
        q = Queue()
        q.enqueue(self.root)
        lastnode =  None
        parentlastnode = None
        
        while not q.is_empty():
            current = q.peek()
            q.dequeue()
            
            if current.lc :
                q.enqueue(current.lc)
                parentlastnode = current
            if current.rc:
                q.enqueue(current.rc)
                parentlastnode = current
                
            lastnode= current
        if lastnode and parentlastnode:
            if parentlastnode.lc == lastnode:
                parentlastnode.lc = None
            else:
                parentlastnode.rc = None
        else:
            self.root = None
    def lowestca(self,root,p,q):
        if root is None:
            return None
        if root.data==p or root.data==q:
            return root
        left_lca=self.lowestca(root.lc,p,q)
        right_lca=self.lowestca(root.rc,p,q)
        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca 
            
obj = BTree()
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
                 
        
                    
                