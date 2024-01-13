from array import array

class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.values = array('l', [0] * (stack_size * 3))
        self.sizes = array('l', [0] * 3)

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            self.expand(stack_num)
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return None
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_num] -= 1
        return value

    def display(self):
        for i in range(3):
            start = i * self.stack_size
            end = start + self.sizes[i]
            print(f"Stack {i}: {self.values[start:end]}")

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return None
        return self.values[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        size = self.sizes[stack_num]
        return offset + size - 1

    def expand(self, stack_num):
        new_values = array('l', [0] * (len(self.values) + 1))
        new_sizes = list(self.sizes)
        
        for i in range(3):
            new_start = i * (self.stack_size + 1)
            new_end = new_start + new_sizes[i]
            old_start = i * self.stack_size
            old_end = old_start + self.sizes[i]

            new_values[new_start:new_end] = self.values[old_start:old_end]
        
        self.stack_size += 1
        self.values = new_values
        self.sizes = array('l', new_sizes)

#user interactive driver code 
stack_size = int(input("Enter the size for each stack: "))
stack = ThreeStacks(stack_size)
print("\nOptions:")
print("1. Push")
print("2. Pop")
print("3. Display")
print("4. Peek")
print("5. Exit")

while True:
    
    choice = input("Enter your choice: ")

    if choice == '1':
        stack_num = int(input("Enter stack number (0, 1, or 2): "))
        data = int(input("Enter data to push: "))  # Convert the input to an integer
        stack.push(stack_num, data)
        print("Pushed", data, "into stack", stack_num)
    elif choice == '2':
        stack_num = int(input("Enter stack number (0, 1, or 2): "))
        try:
            data = stack.pop(stack_num)
            print("Popped", data, "from stack", stack_num)
        except IndexError as e:
            print(e)
    elif choice == '3':
        stack.display()
    elif choice == '4':
        stack_num = int(input("Enter stack number (0, 1, or 2): "))
        try:
            data = stack.peek(stack_num)
            print("Top of stack", stack_num, ":", data)
        except IndexError as e:
            print(e)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        
