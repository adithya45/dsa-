from array import array

class queuee:
    def __init__(self,ms):
        self.ms=ms
        self.queue = array([0]*self.ms)
        self.front=0
        self.rear=-1
    def insert(self,ele):
        self.rear+=1
        self.queue[self.rear]=ele

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        for i in range(self.front,self.rear+1):
            print(self.queue[i])
    
ms = int(input("size"))
obj=queuee(ms)
while True:
    choice=int(input("enter your choice:"))
    if choice == 1:
        ele=int(input("Enter element to be inserted : "))
        obj.insert(ele)
    elif choice == 2:
        obj.display()
    else:
        break
    
    