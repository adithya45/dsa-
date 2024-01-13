class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkl():
    def __init__(self):
        self.head=None
    def countNodes(self):
        temp = self.head  
        count = 0  
        while (temp):
            count += 1
            temp = temp.next
        return count
    def insertf(self,data):
        nn=Node(data)
        nn.next=self.head
        self.head=nn
    def insertend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert(self,data,pos):
        if(pos==1):
            self.insertf(data)
        elif(pos==self.countNodes()+1):
            self.insertend(data)
        else:
            nn=Node(data)
            i=0
            temp=self.head
            while (i<pos-1):
                ptr=temp
                temp=temp.next
                i+=1
            nn.next=temp
            ptr.next=nn
    def delf(self):
        self.heaf=self.head.next
    def dellast(self):
        temp=self.head
        while (temp.next.next!=None):
            temp=temp.next
        temp.next=None
    def delete(self,pos):
        if(pos==1):
            self.delf()
        elif(pos==self.countNodes()+1):
            self.dellast()
        else:
            i=0
            temp=self.head
            while(i<pos-1):
                ptr=temp
                temp=temp.next
                i+=1
            ptr.next=temp.next
    def display(self):
        ptr=self.head
        while(ptr):
            print(ptr.data)
            ptr=ptr.next
    def search(self,ele):
        ptr=self.head
        while(ptr):
            if(ptr.data==ele):
                return "element found"
            ptr=ptr.next
        return 0
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    