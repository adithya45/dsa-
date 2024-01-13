class mystack:
    def __init__(self, ms):
        self.ms = ms
        self.stack = [''] * ms
        self.top = -1

    def isfull(self):
        return self.top == self.ms - 1

    def isempty(self):
        return self.top == -1

    def append(self, ele):
        self.top += 1
        self.stack[self.top] = ele

    def pop(self):
        popped_element = self.stack[self.top]
        self.top -= 1
        return popped_element
    def peak(self):
        return self.stack[self.top]

def precedence(token):
    if token in ('+', '-'):
        return 1
    elif token in ('*', '/'):
        return 2
    elif token == '^':
        return 3
    else:
        return 0

def infix_to_postfix(expression):
    output = []
    stack = mystack(len(expression))

    for token in expression:
        if token.isalnum() or token.isalpha():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while not stack.isempty() and stack.peak() != '(':
                output.append(stack.pop())
            if not stack.isempty() and stack.peak() == '(':
                stack.pop()  # Pop the '(' from the stack
        elif token in ('+', '-', '*', '/'):
            while not stack.isempty() and precedence(stack.peak()) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)


    while not stack.isempty():
        output.append(stack.pop())

    return ''.join(output)

expression = input('Enter infix expression: ')
postfix_expression = infix_to_postfix(expression)
print(postfix_expression)
