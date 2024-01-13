class FlexibleStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)
        self.sizes = [0, 0, 0]  # To keep track of the sizes of the three stacks

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size
    def all_full(self):
        return all(self.is_full(stack_num) for stack_num in range(3))
    def push(self, stack_num, data):
        if self.is_full(stack_num):
            self.expand(stack_num)
        self.sizes[stack_num] += 1
        top_index = self.get_top_index(stack_num)
        self.array[top_index] = data

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise IndexError("Stack Underflow")
        top_index = self.get_top_index(stack_num)
        data = self.array[top_index]
        self.array[top_index] = None
        self.sizes[stack_num] -= 1
        return data

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise IndexError("Stack is empty")
        top_index = self.get_top_index(stack_num)
        return self.array[top_index]

    def get_top_index(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def expand(self, stack_num):
        next_stack = (stack_num + 1) % 3
        if self.all_full():
             raise IndexError("Stack Overflow")
        elif self.sizes[next_stack] >= self.stack_size:
            # If the next stack is also full, expand it first
             self.expand(next_stack)
        # Shift elements from the current stack to the next
        while not self.is_empty(stack_num):
            next_index = self.get_top_index(next_stack)
            current_index = self.get_top_index(stack_num)
            self.array[next_index] = self.array[current_index]
            self.array[current_index] = None
            self.sizes[stack_num] -= 1
            self.sizes[next_stack] += 1
            
stack_size = int(input("Enter the size for each stack: "))
stack = FlexibleStacks(stack_size)

while True:
    print("\nOptions:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peek")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        stack_num = int(input("Enter stack number (0, 1, or 2): "))
        data = input("Enter data to push: ")
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
        print("Stacks:")
        for i in range(3):
            print("Stack", i, ":", stack.array[i * stack_size:(i + 1) * stack_size])
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
