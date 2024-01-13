from singlelinkedlist import *
class Queue:
    def __init__(self):
        self.queue=linkl()
    def insert(self,ele):
        if self.queue.isempty():
            self.queue.insertf(ele)
        else:
            self.queue.insertend(ele)
    def delete(self):
        self.queue.delf()
    def peek(self):
        if self.queue.isempty():
            print('queue is empty')
        else:
            return(self.queue.head.data)
    def display(self):
        self.queue.display()
obj=Queue()
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
        obj.insert(value)
    elif(choice=='2'):
        obj.delete()
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
