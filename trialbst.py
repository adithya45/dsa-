class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
    def _insert_recursive(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.data:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.data:
            root.right = self._insert_recursive(root.right, key)
        return root
    def findmax(self):
        cn = self.root
        if self.root is None:
            return None
        else:
            while cn.right is not None:
                cn = cn.right
            max_val = cn.data
            return max_val
    def search(self, key):
        cn = self.root
        while cn is not None and cn.data != key:
            if cn.data > key:
                cn = cn.left
            elif cn.data < key:
                cn = cn.right
        if cn is not None:
            print("Given key is found in the Binary Search Tree")
        else:
            print("Given key is not found in the Binary Search Tree")
    def delete_node(self,root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.find_min_value(root.right)
            root.right = self.delete_node(root.right, root.data)
        return root

    def find_min_value(self,node):
        # Helper function to find the smallest value in a BST
        current = node
        while current.left is not None:
            current = current.left
        return current.data
    def inorder(self, cn):
        if cn is not None:
            self.inorder(cn.left)
            print(cn.data, end=", ")
            self.inorder(cn.right)
    def sumleftleaf(self):
        cn=self.root
        sum=cn.data
        while cn.left!=None:
            cn=cn.left
            sum+=cn.data            
        return sum
            
            
            
bst = BST()
for key in [10, 5, 15, 3, 8]:
    bst.insert(key)

print("Before Deletion:")
bst.inorder(bst.root)
print()
bst.delete_node(bst.root,5)

print("After Deletion:")
bst.inorder(bst.root)
print()
print("the sum of left leafs is")
print(bst.sumleftleaf())