class Hash:
    def __init__(self, size):
        self.D = size
        self.ht = [0] * self.D
        self.empty = [True] * self.D

    def insert(self, ele):
        i = ele % self.D
        if self.empty[i]:
            self.ht[i], self.empty[i] = ele, False
        else:
            j = (i + 1) % self.D
            while j != i and not self.empty[j]:
                j = (j + 1) % self.D
            if j == i:
                print("\n Hash Table is Full")
                return
            self.ht[j], self.empty[j] = ele, False

    def search(self, ele):
        i = ele % self.D
        j = i
        while True:
            if self.ht[i] == ele and not self.empty[i]:
                return i
            i = (i + 1) % self.D
            if i == j or self.empty[i]:
                break
        return -1

    def delete(self, ele):
        i = self.search(ele)
        if i != -1:
            self.ht[i], self.empty[i] = 0, True
            print("\n Deleted element is:", ele)
        else:
            print("\n Element does not exist")

    def display(self):
        print("\n Hash Table elements are:", end="\t")
        for i in range(self.D):
            print(self.ht[i] if not self.empty[i] else "-", end="\t")
        print()

def menu():
    return int(input("1.Insert\n2.Delete\n3.Display\n4.Search\n5.Exit\nEnter your choice: "))

def main():
    obj = Hash(11)
    ch = menu()

    while ch != 5:
        if ch == 1:
            ele = int(input("\nEnter element: "))
            obj.insert(ele)
        elif ch == 2:
            ele = int(input("\nEnter the element to be deleted: "))
            obj.delete(ele)
        elif ch == 3:
            obj.display()
        elif ch == 4:
            ele = int(input("\nEnter the element to be searched: "))
            i = obj.search(ele)
            print("\nElement found at index:", i) if i != -1 else print("\nElement not found")

        ch = menu()

if __name__ == "__main__":
    main()
