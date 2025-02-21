class BSTEntry:
    def __init__(self, data, key):
        self.data = data
        self.key = key
    
    def __str__(self):
        return f"Key: {self.key}, Data: {self.data}"

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data, key):
        """Inserta un nuevo dato con su clave"""
        entry = BSTEntry(data, key)
        if not self.root:
            self.root = Node(entry)
        else:
            self._insert_recursive(self.root, entry)
    
    def _insert_recursive(self, node, entry):
        if entry.key < node.entry.key:
            if node.left is None:
                node.left = Node(entry)
            else:
                self._insert_recursive(node.left, entry)
        else:
            if node.right is None:
                node.right = Node(entry)
            else:
                self._insert_recursive(node.right, entry)
    
    def find(self, key):
        """Busca un nodo por su clave"""
        return self._find_recursive(self.root, key)
    
    def _find_recursive(self, node, key):
        if node is None or node.entry.key == key:
            return node
        if key < node.entry.key:
            return self._find_recursive(node.left, key)
        return self._find_recursive(node.right, key)
    
    def remove(self, key):
        """Elimina un nodo por su clave"""
        self.root = self._remove_recursive(self.root, key)
    
    def _remove_recursive(self, node, key):
        if node is None:
            return None
        
        if key < node.entry.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.entry.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            # Nodo con un solo hijo o sin hijos
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Nodo con dos hijos
            min_node = self._find_min_node(node.right)
            node.entry = min_node.entry
            node.right = self._remove_recursive(node.right, min_node.entry.key)
        
        return node
    
    def find_max(self):
        """Encuentra el valor máximo en el árbol"""
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.entry
    
    def find_min(self):
        """Encuentra el valor mínimo en el árbol"""
        if not self.root:
            return None
        return self._find_min_node(self.root).entry
    
    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def inorder(self):
        """Realiza un recorrido inorder del árbol"""
        print("Recorrido Inorder:")
        self._inorder_recursive(self.root)
        print()
    
    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(f"{node.entry.key} ({node.entry.data})", end=" ")
            self._inorder_recursive(node.right)
    
    def print_tree(self):
        """Imprime la estructura del árbol"""
        print("Estructura del Arbol Binario de Busqueda:")
        self._print_tree_recursive(self.root, "", True)
    
    def _print_tree_recursive(self, node, prefix, is_left):
        if node:
            print(prefix + ("|-- " if is_left else "`-- ") + 
                  f"{node.entry.key} ({node.entry.data})")
            self._print_tree_recursive(node.left, prefix + ("|   " if is_left else "    "), True)
            self._print_tree_recursive(node.right, prefix + ("|   " if is_left else "    "), False)

def test_bst():
    bst = BinarySearchTree()
    
    # Insertar los datos de prueba
    test_data = [
        ("Juan", 7),    # 10101013
        ("Pablo", 4),   # 10001011
        ("Maria", 9),   # 10101015
        ("Ana", 2),     # 1010000
        ("Diana", 10),  # 10111105
        ("Mateo", 8),   # 10110005
    ]
    
    for nombre, key in test_data:
        bst.insert(nombre, key)
    
    # Mostrar la estructura del árbol
    print("\nArbol inicial:")
    bst.print_tree()
    
    # Mostrar recorrido inorder
    print("\nRecorrido inorder:")
    bst.inorder()
    
    # Encontrar mínimo y máximo
    min_entry = bst.find_min()
    max_entry = bst.find_max()
    print(f"\nValor minimo: {min_entry.key} ({min_entry.data})")
    print(f"Valor maximo: {max_entry.key} ({max_entry.data})")
    
    # Buscar un valor
    search_key = 7
    found = bst.find(search_key)
    print(f"\nBuscando clave {search_key}: {found.entry.data if found else 'No encontrado'}")
    
    # Eliminar un nodo
    remove_key = 4
    print(f"\nEliminando clave {remove_key} (Pablo)")
    bst.remove(remove_key)
    print("Arbol actualizado:")
    bst.print_tree()

if __name__ == "__main__":
    test_bst()