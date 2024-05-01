class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.key)
            result += self._preorder_traversal(root.left)
            result += self._preorder_traversal(root.right)
        return result

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        result = []
        if root:
            result += self._inorder_traversal(root.left)
            result.append(root.key)
            result += self._inorder_traversal(root.right)
        return result

    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, root):
        result = []
        if root:
            result += self._postorder_traversal(root.left)
            result += self._postorder_traversal(root.right)
            result.append(root.key)
        return result

    def level_order_traversal(self):
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.key)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        else:
            left_height = self._height(root.left)
            right_height = self._height(root.right)
            return max(left_height, right_height) + 1

    def occurrences(self, key):
        return self._occurrences(self.root, key)

    def _occurrences(self, root, key):
        if root is None:
            return 0
        count = 0
        if root.key == key:
            count = 1
        count += self._occurrences(root.left, key)
        count += self._occurrences(root.right, key)
        return count

    def count_even_odd(self):
        even_count = 0
        odd_count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                if node.key % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
                stack.append(node.left)
                stack.append(node.right)
        return even_count, odd_count

# Crear un árbol de ejemplo
tree = BinarySearchTree()
numbers = [50, 30, 70, 20, 40, 60, 80]
for num in numbers:
    tree.insert(num)

# Ejemplo de uso de las funciones
print("Recorrido preorden:", tree.preorder_traversal())
print("Recorrido inorden:", tree.inorder_traversal())
print("Recorrido postorden:", tree.postorder_traversal())
print("Recorrido por nivel:", tree.level_order_traversal())
print("Altura del árbol:", tree.height())
print("Cantidad de ocurrencias de 30:", tree.occurrences(30))
even_count, odd_count = tree.count_even_odd()
print("Cantidad de números pares e impares:", even_count, odd_count)

# Determinar si un número está cargado en el árbol
number_to_search = 30
if tree.search(number_to_search):
    print(f"El número {number_to_search} está en el árbol.")
else:
    print(f"El número {number_to_search} no está en el árbol.")

# Eliminar tres valores del árbol
numbers_to_delete = [20, 40, 60]
for num in numbers_to_delete:
    tree.delete(num)

# Determinar la altura del subárbol izquierdo y del subárbol derecho
left_subtree_height = tree._height(tree.root.left)
right_subtree_height = tree._height(tree.root.right)
print("Altura del subárbol izquierdo:", left_subtree_height)
print("Altura del subárbol derecho:", right_subtree_height)