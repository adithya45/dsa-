from slll import *
class Queue:
    def __init__(self):
        self.queue=llist()
    def enqueue(self,ele):
        if self.queue.isempty():
            self.queue.insertatfirst(ele)
        else:
            self.queue.insertatend(ele)
    def dequeue(self):
        return self.queue.deletefirst()
    def peek(self):
        if self.queue.isempty():
            print('queue is empty')
        else:
            return(self.queue.head.data)
    def display(self):
        self.queue.display()
    def is_empty(self):
        if self.queue.isempty():
            return True
        else:
            return False
obj=Queue()

