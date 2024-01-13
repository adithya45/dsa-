class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None 
class DELL:
    def __init__(self):
        self.head=None
    def isempty(self):
        if(self.head==None):
            return True
    def insertbegin(self,val):
        newnode=node(val)
        if(self.isempty()):
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.previous=newnode
            self.head=newnode
    def insertmiddle(self,val,pos):
        i=0
        if(self.isempty()):
            self.insertbegin()
        else:
            temp=self.head
            i=0
            newnode=node(val)
            while(i<pos-1):
                temp=temp.next
                i+=1
            newnode.previous=temp
            newnode.next=temp.next
            temp.next.previous=newnode
            temp.next=newnode
    def insertend(self,val):
        temp=self.head
        newnode=node(val)
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
        newnode.previous=temp
    def deletebegin(self):
        if(self.isempty()):
            print('Linked list is empty')
        else:
            self.head.next.previous=None
            self.head=self.head.next
    def deletemiddle(self,pos):
        i=0
        temp=self.head
        while(i<pos-1):
            i+=1
            temp=temp.next
        temp.next.next.previous=temp
        temp.next=temp.next.next
    def deleteend(self):
        if(self.isempty()):
            print('linked list is empty')
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
print('''MENU
    1)insertbegin
    2)insertmiddle
    3)insertend
    4)deletebegin
    5)deletemiddle
    6)deleteend
    7)display
    8)exit''')
obj=DELL()
while(True):
    x=input('enter your choice')
    if(x=='1'):
        obj.insertbegin(int(input('enter the value')))
    elif(x=='2'):
        obj.insertmiddle(int(input('enter the value')),int(input('enter the index')))
    elif(x=='3'):
        obj.insertend(int(input('enter the value')))
    elif(x=='4'):
        obj.deletebegin()
    elif(x=='5'):
        obj.deletemiddle(int(input('enter the index')))
    elif(x=='6'):
        obj.deleteend()
    elif(x=='7'):
        obj.display()
    elif(x=='8'):
        print('exiting the program')
        break
    else:
        print('select valid option')