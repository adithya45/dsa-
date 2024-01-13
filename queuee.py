from array import array
class myqueue:
    def __init__(self,size):
        self.size=size
        self.queue=array("i",[0]*size)
        self.rear=self.front=-1
    def is_full(self):
        return(self.rear+1)%self.size == self.front
    def is_empty(self):
        return self.rear==-1
    def enqueue(self,item):
        if self.is_full():
            print("queue is full cannot enqueue")
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=item

    def dequeue(self):
        if self.is_empty():
            print("queue is empty cannot dequeue")
            return None
        else:
            removed_item=self.queue[self.front]
            if self.front==self.rear:
                self.front=self.rear=-1
            else:
                self.front=(self.front+1)%self.size
            return removed_item
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()
ms=int(input("enter the size:"))
obj=myqueue(ms)
print('\n Menu')
print('1.Insert')
print('2.Delete')
print('3.peek')
print('4.display')
print('5.exit')
while True:
    choice=input('enter your choice')
    if choice=='1':
        value=int(input('Enter the value to push'))
        obj.enqueue(value)
    elif(choice=='2'):
        obj.dequeue()
    elif(choice=='3'):
        top_value=obj.peek()
        print('peek value',top_value)
    elif choice=='4':
        obj.display()
    elif choice=='5':
        print('exiting the program')
        break
    else:
        print('INVALID CHOICE')
