from array import array
class queue:
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