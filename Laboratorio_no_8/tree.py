class BSTEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f"Clave: {self.key}, Valor: {self.value}"

class BinaryTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
        self.entry = None
        
    def is_empty(self):
        return self.root is None

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
        
    def insert(self, key, value):
        entry = BSTEntry(key, value)
        if self.is_empty():
            self.root = BinarySearchTree()
            self.root.entry = entry
            return
            
        if key <= self.root.entry.key:
            if self.root.left is None:
                self.root.left = BinarySearchTree()
                self.root.left.root = BinarySearchTree()
                self.root.left.root.entry = entry
            else:
                self.root.left.insert(key, value)
        else:
            if self.root.right is None:
                self.root.right = BinarySearchTree()
                self.root.right.root = BinarySearchTree()
                self.root.right.root.entry = entry
            else:
                self.root.right.insert(key, value)
    
    def find(self, key):
        if self.is_empty():
            return None
            
        if self.root.entry.key == key:
            return self.root.entry
            
        if key < self.root.entry.key and self.root.left:
            return self.root.left.find(key)
        elif key > self.root.entry.key and self.root.right:
            return self.root.right.find(key)
            
        return None
        
    def find_min(self):
        if self.is_empty():
            return None
            
        current = self
        while current.root.left:
            current = current.root.left
        return current.root.entry
        
    def find_max(self):
        if self.is_empty():
            return None
            
        current = self
        while current.root.right:
            current = current.root.right
        return current.root.entry
        
    def delete(self, key):
        if self.is_empty():
            return self
            
        if key < self.root.entry.key:
            if self.root.left:
                self.root.left = self.root.left.delete(key)
        elif key > self.root.entry.key:
            if self.root.right:
                self.root.right = self.root.right.delete(key)
        else:
            if not self.root.left and not self.root.right:
                return None
            elif not self.root.left:
                return self.root.right
            elif not self.root.right:
                return self.root.left
            else:
                min_node = self.root.right.find_min()
                self.root.entry = min_node
                self.root.right = self.root.right.delete(min_node.key)
                
        return self
        
    def inorder_traversal(self):
        result = []
        if not self.is_empty():
            if self.root.left:
                result.extend(self.root.left.inorder_traversal())
            result.append(str(self.root.entry))
            if self.root.right:
                result.extend(self.root.right.inorder_traversal())
        return result
        
    def display(self, level=0, prefix="Raiz: "):
        if self.is_empty():
            return ""
            
        ret = "  " * level + prefix + str(self.root.entry) + "\n"
        if self.root.left:
            ret += self.root.left.display(level + 1, "I--- ")
        if self.root.right:
            ret += self.root.right.display(level + 1, "D--- ")
        return ret

def sum_digits(number):
    return sum(int(digit) for digit in str(number))

def test_bst():
    bst = BinarySearchTree()
    
    test_data = [
        ("Juan", 10101013),
        ("Pablo", 10001011),
        ("Maria", 10101015),
        ("Ana", 1010000),
        ("Diana", 10111105),
        ("Mateo", 10110005)
    ]
    
    for name, id_number in test_data:
        key = sum_digits(id_number)
        bst.insert(key, name)
        
    print("Binary Search Tree :")
    print(bst.display())
    
    print("\nInorder:")
    print(", ".join(bst.inorder_traversal()))
    
    print("\nValor minimo:", bst.find_min())
    print("Valor maximo:", bst.find_max())
    
    # Test search
    search_key = 7  # Should find Juan
    result = bst.find(search_key)
    print(f"\nBuscando la clave {search_key}:", result)
    
    # Test deletion
    print("\nEliminando la clave 7 (Juan)")
    bst.delete(7)
    print("\nArbol actualizado:")
    print(bst.display())

test_bst()