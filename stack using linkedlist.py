#stack using linked list
from singlelinkedlist import *
class Stack:
    def __init__(self):
        self.stack=linkl()
    def push(self,ele):
        self.stack.insertend(ele)
    def pop(self):
        self.stack.dellast()
    def display(self):
        self.stack.display()
    def peek(self):
        if(self.stack.isempty()):
            print('linked list is empty')
        else:
            return(self.stack.head.data) 

obj=Stack()
print('\n Menu')
print('1.Push')
print('2.pop')
print('3.top')
print('4.display')
print('5.exit')
while True:
    choice=input('enter your choice')
    if choice=='1':
        value=int(input('Enter the value to push'))
        obj.push(value)
    elif(choice=='2'):
        obj.pop()
    elif(choice=='3'):
        top_value=obj.peek()
        print('top value',top_value)
    elif choice=='4':
        obj.display()
    elif choice=='5':
        print('exiting the program')
        break
    else:
        print('INVALID CHOICE')
