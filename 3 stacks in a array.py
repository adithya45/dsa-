from array import array

class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.values = array('l', [0] * (stack_size * 3))  # Create an array to store values
        self.sizes = array('l', [0] * 3)  # Create an array to store sizes of stacks

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            self.expand(stack_num)
        self.sizes[stack_num] += 1  # Increase the size of the stack
        self.values[self.index_of_top(stack_num)] = value  # Push the value to the top of the stack

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return None
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]  # Get the value at the top
        self.values[top_index] = 0  # Set the top to 0 to remove the value
        self.sizes[stack_num] -= 1  # Decrease the size of the stack
        return value

    def display(self):
        for i in range(3):
            start = i * self.stack_size
            end = start + self.sizes[i]
            print(f"Stack {i}: {self.values[start:end]}")

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return None
        return self.values[self.index_of_top(stack_num)]  # Get the value at the top

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        size = self.sizes[stack_num]
        return offset + size - 1  # Calculate the index of the top element

    def next_index(self, index):
        return (index + 1) % len(self.values)

    def prev_index(self, index):
        return (index - 1) % len(self.values)

    def expand(self, stack_num):
        self.shift((stack_num + 1) % 3)
        self.sizes[stack_num] += 1

    def shift(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            self.shift((stack_num + 1) % 3)
            self.sizes[stack_num] += 1
        index = self.index_of_top(stack_num)
        while self.is_within_stack_range(index):
            prev_index = self.prev_index(index)
            self.values[index] = self.values[prev_index]  # Shift elements within the stack
            index = prev_index
        self.values[self.index_of_top(stack_num)] = 0  # Remove the element at the top
        self.sizes[stack_num] -= 1

    def is_within_stack_range(self, index):
        if index < 0 or index >= len(self.values):
            return False
        contiguous_index = index + len(self.values) if index < self.stack_size else index
        end = self.index_of_top(2)
        return self.stack_size * 2 <= contiguous_index <= end

if __name__ == "__main__":
    stack_size = int(input("Enter the size for each stack: "))
    three_stacks = ThreeStacks(stack_size)

    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice (1/2/3/4/5): "))

        if choice == 1:
            stack_num = int(input("Enter the stack number (0/1/2): "))
            value = int(input("Enter the value to push: "))
            three_stacks.push(stack_num, value)
        elif choice == 2:
            stack_num = int(input("Enter the stack number (0/1/2): "))
            value = three_stacks.pop(stack_num)
            if value is not None:
                print(f"Popped value from Stack {stack_num}: {value}")
        elif choice == 3:
            stack_num = int(input("Enter the stack number (0/1/2): "))
            value = three_stacks.peek(stack_num)
            if value is not None:
                print(f"Top value in Stack {stack_num}: {value}")
        elif choice == 4:
            three_stacks.display()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
