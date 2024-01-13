class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def insertatfirst(self,val):
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
    def count(self):
        CN=self.head
        c=0
        while CN != None:
            c+=1
            CN=CN.next
        return c
    def display(self):
        CN=self.head
        while CN != None:
            print(CN.data)
            CN=CN.next
    def search(self,val):
        CN=self.head
        while CN != None:
            if CN.data==val:
                return 1
            CN=CN.next
        return 0
    def insertatend(self,val):
        newnode=Node(val)
        cn=self.head
        while cn.next != None:
            cn=cn.next
        cn.next=newnode
    def insert(self,ele,pos):
        newnode=Node(ele)
        if pos==1:
            self.insertatfirst(ele)
        elif pos>=(self.count())+1:
            self.insertatend(ele)
        else:
            cn=self.head
            i=1
            while i<pos-1:
                cn=cn.next
                i=i+1
            newnode.next=cn.next
            cn.next=newnode
    def deletefirst(self):
        if self.head== None:
            print("list is empty")
        else:
            temp=self.head
            self.head=self.head.next
        return temp.data
    def deleteatlast(self):
        if self.head== None:
            print("list is empty")
        else:
            temp=self.head
            while temp.next != None:
                prev=temp
                temp=temp.next
                i+=1
            prev.next=temp.next
            temp=None
    def delete(self,pos):
        if pos==1:
            self.deletefirst()
        elif pos>=self.count()+1:
            self.deleteatlast()
        else:
            cn=self.head
            i=1
            while i<pos:
                prev=cn
                cn=cn.next
                i+=1
            prev.next=cn.next
            print("deleted element is ",cn.data)
            cn=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def hascycle(self):
        if not self.head and self.head.next:
            return False
        slow=self.head
        fast=self.head.next
        while fast and fast.next:
            if slow==fast:
                return False
            slow=slow.next
            fast=fast.next.next
        return False
    def partition(self, x):
        if not self.head or not self.head.next:
            return

        # Create two separate linked lists for values less than x and greater than or equal to x
        less_than_x = llist()
        greater_than_equal_to_x = llist()

        current = self.head

        while current:
            if current.data < x:
                less_than_x.insertatend(current.data)
            else:
                greater_than_equal_to_x.insertatend(current.data)
            current = current.next

        # Concatenate the two lists
        if less_than_x.head:
            self.head = less_than_x.head
            last_node = less_than_x.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = greater_than_equal_to_x.head
        else:
            self.head = greater_than_equal_to_x.head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
ll = llist()
ll.insertatfirst(1)
ll.insertatend(4)
ll.insertatend(3)
ll.insertatend(2)
ll.insertatend(5)

print("Original Linked List:")
ll.display()

x = 3
ll.partition(x)

print(f"\nLinked List after partitioning at {x}:")
ll.display()

        
        
        
        