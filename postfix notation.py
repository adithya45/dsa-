class mystack:
    def __init__(self, ms):
        self.ms = ms
        self.stack = [''] * ms
        self.top = -1

    def isfull(self):
        return self.top == self.ms - 1

    def isempty(self):
        return self.top == -1

    def push(self, ele):
        self.top += 1
        self.stack[self.top] = ele

    def pop(self):
        popped_element = self.stack[self.top]
        self.top -= 1
        return popped_element
    def peak(self):
        return self.stack[self.top]
output = []
def valuation(exp):
    obj = mystack(len(exp))  
    for i in exp:
        if i not in l:
            obj.push(int(i))  
        elif i in l:
            if obj.isempty():
                return None
            else:
                b2 = obj.pop()
                b1 = obj.pop()
                result = math(b1, i, b2) 
                obj.push(result)  
    if obj.isempty():
        return None
    return obj.pop()  

def math(b1, i, b2):
    if i == "+":
        return b1 + b2
    elif i == "-":
        return b1 - b2
    elif i == "*":
        return b1 * b2
    elif i == "/":
        if b2 == 0:
            raise ValueError("Division by zero")
        return b1 / b2
    elif i == "^":
        return b1 ** b2
exp =input("enter postfix expression with each value separated by comma").split(",")
obj=mystack(len(exp))  # Split and convert to integers
l = ["+", "-", "*", "/", "^"]
a = valuation(exp)
print(a)
