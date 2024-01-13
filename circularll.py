class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class circular():
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def insertfirst(self,val):
        newnode=Node(val)
        if self.isempty():
            self.head=newnode
            self.head.next=newnode
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
            self.head=newnode
    def insertlast(self,val):
        newnode=Node(val)
        if self.isempty():
            self.head=newnode
            self.head.next=newnode
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
    def insertposition(self,val,pos):
        newnode=Node(val)
        if self.isempty():
            self.insertfirst(val)
        elif pos==1:
            self.insertfirst(val)
        elif pos>=self.count():
            self.insertlast(val)
        else:
            temp=self.head
            i=1
            while i<pos-1:
                temp=temp.next
                i+=1
            newnode.next=temp.next
            temp.next=newnode
    def deletefirst(self):
        if self.isempty():
            print("linked list is empty")
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
            self.head=None
    def deletelast(self):
        if self.isempty():
            print("linkedlist is empty")
        elif self.count==1:
            self.deletefirst()
        else:
            ptr=self.head
            temp=self.head
            while temp.next!=self.head:
                ptr=temp
                temp=temp.next
            ptr.next=self.head
            self.head=None
    def deleteposition(self,pos):
        if self.isempty():
            print("linkedlist is empty")
        elif pos==1:
            self.deletefirst()
        elif pos>=self.count():
            self.deletelast()
        else:
            i=1
            temp=self.head
            prev=self.head
            while i<pos-1:
                prev=temp
                temp=temp.next
                i+=1
            prev.next=temp.next
            
    def count(self):
        temp=self.head
        c=1
        while temp.next!=self.head:
            c+=1
            temp=temp.next
        return c
            
    def display(self):
        if self.isempty():
            print("linkedlist is empty")
        else:
            temp=self.head
            while temp.next!=self.head:
                print(temp.data)
                temp=temp.next
            print(temp.data)
obj=circular()
print("\nMenu\n1.Insertbegin\n2.Insertlast\n3.Insertposition\n4.Deletefirst\n5.Deletelast\n6.Deleteposition\n7.Count\n8.Display\n9.Exit")
while True:
    choice=int(input("enter your choice:"))
    if choice==1:
        ele=int(input("enter number to insert"))
        obj.insertfirst(ele)
    elif choice==2:
        ele=int(input("enter number to insert"))
        obj.insertlast(ele)
    elif choice==3:
        ele=int(input("enter number to insert"))
        pos=int(input("enter position to insert"))
        obj.insertposition(ele,pos)
    elif choice==4:
        obj.deletefirst()
    elif choice==5:
        obj.deletelast()
    elif choice==6:
        pos=int(input("enter position to delete"))
        obj.deleteposition(pos)
    elif choice==7:
        s=obj.count()
        print("number of nodes:",s)
    elif choice==8:
        obj.display()
    elif choice==9:
        print("program terminated successfully")
        break
