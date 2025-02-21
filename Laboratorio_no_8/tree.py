class Node:
    def __init__(self, name: str, id_number: int):
        self._name = name
        self._id_number = id_number
        self._key = sum(int(digit) for digit in str(id_number))  
        self._left = None
        self._right = None
    
    @property
    def name(self):
        return self._name
    
    @property
    def id_number(self):
        return self._id_number
    
    @property
    def key(self):
        return self._key
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, left):
        self._left = left
    
    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, right):
        self._right = right
    
    def __str__(self):
        return f"Nombre: {self._name}, ID: {self._id_number}, Clave: {self._key}"

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0
    
    def is_empty(self) -> bool:
        return self._root is None
    
    def size(self) -> int:
        return self._size
    
    def root(self) -> Node:
        return self._root
    
    def left(self, v: Node) -> Node:
        return v.left if v else None
    
    def right(self, v: Node) -> Node:
        return v.right if v else None
    
    def depth(self, v: Node) -> int:
        if not v:
            return -1
        return 1 + max(self.depth(v.left), self.depth(v.right))
    
    def height(self) -> int:
        return self.depth(self._root)
    
    def has_left(self, v: Node) -> bool:
        return v.left is not None if v else False
    
    def has_right(self, v: Node) -> bool:
        return v.right is not None if v else False

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    
    def find(self, k: int) -> Node:
        return self._find_helper(self._root, k)
    
    def _find_helper(self, node: Node, k: int) -> Node:
        if not node:
            return None
        if k == node.key:
            return node
        if k < node.key:
            return self._find_helper(node.left, k)
        else:
            return self._find_helper(node.right, k)
    
    def insert(self, name: str, id_number: int) -> None:
        new_node = Node(name, id_number)
        if self.is_empty():
            self._root = new_node
            self._size = 1
            return
        self._insert_helper(self._root, new_node)
    
    def _insert_helper(self, current: Node, new_node: Node) -> None:
        if new_node.key < current.key:
            if not current.left:
                current.left = new_node
                self._size += 1
            else:
                self._insert_helper(current.left, new_node)
        else:
            if not current.right:
                current.right = new_node
                self._size += 1
            else:
                self._insert_helper(current.right, new_node)
    
    def inorder_traversal(self):
        result = []
        self._inorder_helper(self._root, result)
        return result
    
    def _inorder_helper(self, node: Node, result: list):
        if node:
            self._inorder_helper(node.left, result)
            result.append(str(node))
            self._inorder_helper(node.right, result)
    
    def display(self):
        return self._display_helper(self._root, "", True)
    
    def _display_helper(self, node: Node, prefix: str, is_left: bool) -> str:
        if not node:
            return ""
        
        result = prefix
        result += "I-- " if is_left else "D-- "
        result += str(node) + "\n"
        
        if node.left:
            result += self._display_helper(node.left, prefix + ("|   " if not is_left else "    "), True)
        if node.right:
            result += self._display_helper(node.right, prefix + ("|   " if not is_left else "    "), False)
            
        return result

def test_binary_search_tree():
    bst = BinarySearchTree()
    
    datos = [
        ("Juan", 10101013),   # k=7
        ("Pablo", 10001011),  # k=4
        ("Maria", 10101015),  # k=9
        ("Ana", 1010000),     # k=2
        ("Diana", 10111105),  # k=10
        ("Mateo", 10110005)   # k=8
    ]
    
    print("Insertando datos...")
    for nombre, id_numero in datos:
        bst.insert(nombre, id_numero)
        print(f"Insertado: {nombre} (ID: {id_numero}, Clave: {sum(int(d) for d in str(id_numero))})")
    
    print("\nEstructura del Arbol:")
    print(bst.display())
    
    print("Recorrido Inorder (ordenado por clave):")
    for node_str in bst.inorder_traversal():
        print(node_str)
    
    clave_buscar = 7  # Debería encontrar a Juan
    resultado = bst.find(clave_buscar)
    print(f"\nBuscando clave {clave_buscar}:")
    print(resultado if resultado else "No encontrado")

if __name__ == "__main__":
    test_binary_search_tree()