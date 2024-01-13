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


max_size = int(input("Enter the maximum size of the stack: "))
obj = Stack(max_size)
while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        value = int(input("Enter the value to push: "))
        obj.push(value)
    elif choice == '2':
        popped_value = obj.pop()
        if popped_value is not None:
            print(f"Popped value: {popped_value}")
    elif choice == '3':
        top_value = obj.peak()
        if top_value is not None:
            print(f"Top value: {top_value}")
    elif choice == '4':
        obj.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
