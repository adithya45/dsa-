class Hash:
    def __init__(self, size):
        self.D = size
        self.ht = [0] * self.D
        self.empty = [True] * self.D
        for i in range(self.D):
            self.ht[i] = 0
            self.empty[i] = True

    def insert(self, ele):
        i = ele % self.D
        if self.empty[i]:
            self.ht[i] = ele
            self.empty[i] = False
        else:
            j = (i + 1) % self.D
            while j != i:
                if self.empty[j]:
                    self.ht[j] = ele
                    self.empty[j] = False
                    return
                j = (j + 1) % self.D
            print("\n Hash Table is Full")
    def search(self,ele):
        i = ele % self.D
        j = i
        while True:
            if self.ht[i] == ele and not self.empty[i]:
                return i
            i = (i + 1) % self.D
            if i == j:
                break
        return -1
    def Delete(self,ele):
        i = self.search(ele)
        if i != -1:
            self.ht[i] = 0
            self.empty[i] = True
            print("\n Deleted element is :", ele)
        else:
            print("\n Element does not exist")
    def display(self):
        print("\n Hash Table elements are...")
        for i in range(self.D):
            print(self.ht[i], end="\t")
            
def menu():
    i = int(input("1.Insert\n2.Delete\n3.Display\n4.search\n5.exit\n"))
    return i


    
obj = Hash(11)
ch = menu()
while ch != 5:
    if ch == 1:
        ele = int(input("\n Enter element:"))
        obj.insert(ele)
    elif ch == 2:
        ele = int(input("\n Enter the element to be deleted:"))
        obj.Delete(ele)
    elif ch == 3:
        obj.display()
    elif ch == 4:
        ele = int(input("\n enter the element to be searched:"))
        i = obj.search(ele)
        if i != -1:
            print("\n element found at", i)
        else:
            print("\n Element not found")
    ch = menu()
