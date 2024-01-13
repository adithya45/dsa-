from array import array
import numpy as np
class circularqueue:
    def __init__(self,ms):
        self.ms=ms
        self.front=-1
        self.rear=-1
        self.queue=np.array([0]*ms)
    def underflow(self):
        if (self.rear==-1 and self.front==self.ms):
            return True
        else:
            return False
    def overflow(self):
        if (self.front==0 and self.rear==self.ms-1) or (self.front==(self.rear+1)%self.ms):
            return True
        else:
            return False
    def push(self,val):
        if self.overflow():
            print("it is full")
        elif self.underflow():
            self.front=0
            self.rear=0
            self.queue[self.rear]=val
        elif self.front!=0 and self.rear==self.ms-1:
            self.rear=0
            self.queue[self.rear]=val
        else:
            self.rear+=1
            self.queue[self.rear]=val
    def pop(self):
        if self.underflow():
            print("it is empty")
        elif self.front==self.rear:
            val=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return val
        else:
            val=self.queue[self.front]
            self.front+=1
            return val
    def peak(self):
        if self.underflow():
            print("it is empty")
        else:
            return self.queue[self.front]
    def display(self):
        if self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
        else:
            for i in range(self.front,self.ms-1):
                print(self.queue[i])
            for i in range(0,self.rear+1):
                print(self.queue[i])
obj=circularqueue(8)
ms=int(input("enter maximum length:"))
while True:
    print("\nMenu:\n1.Push:\n2.Pop\n3.Top\n4.Display\n5.Exit\n")
    choice=int(input("enter your choice:"))
    if choice==1:
        val=input("enter value to push:")
        obj.push(val)
    elif choice==2:
        a=obj.pop()
        print("popped value:",a)
    elif choice==3:
        a=obj.peak()
        print("top value:",a)
    elif choice==4:
        obj.display()
    elif choice==5:
        print("program Terminated Successfully")
        break