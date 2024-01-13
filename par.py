from array import array


class Stack:
    def __init__(self, ms):
        self.ms = ms
        self.stack = array("i", [0] * ms)
        self.top = -1

    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top == self.ms - 1

    def push(self, value):
        if self.isfull():
            print("Stack is full. Cannot push.")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.isempty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_value = self.stack[self.top]
            self.top -= 1
            return popped_value

    def peak(self):
        if self.isempty():
            print("Stack is empty. No top element.")
            return None
        else:
            return self.stack[self.top]

    def display(self):
        if self.isempty():
            print("Stack is empty.")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])


def check(exp, a):
    for i in exp:
        if i == '(':
            obj.push(i)
        elif i == ")" and not (obj.isempty()):
            obj.pop()
        elif i == ")" and obj.isempty():
            a = 'left'
            break
    if obj.isempty() and a == 'right':
        print('PARANTHESIS MATCHED')
    else:
        print('{} PARANTHESIS NOT MATCHED'.format(a))


exp = input('Enter paranthesis expression::')
obj = Stack(len(exp))
a = 'right'
sv = check(exp, a)