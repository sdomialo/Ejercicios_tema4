from TreeNode import TreeNode
class TreeNode:
    def __init__(self, title, page):
        self.title = title
        self.page = page
        self.left = None
        self.right = None

def load_index_from_file(filename):
    index = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            title = parts[0]
            page = int(parts[1])
            index.append((title, page))
    return index

def build_knuth_transform(index):
    if not index:
        return None
    root = TreeNode(index[0][0], index[0][1])
    stack = [root]
    i = 1
    while i < len(index):
        node = TreeNode(index[i][0], index[i][1])
        if stack[-1].left is None:
            stack[-1].left = node
        else:
            while stack[-1].right is not None:
                stack.pop()
            stack[-1].right = node
        if index[i][0].startswith('Chapter'):
            stack.append(node)
        i += 1
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.title, node.page)
        inorder_traversal(node.right)

def find_subtitle(node, subtitle):
    if node is None:
        return
    if node.title == subtitle:
        inorder_traversal(node)
    find_subtitle(node.left, subtitle)
    find_subtitle(node.right, subtitle)

def count_chapters(node):
    if node is None:
        return 0
    count = 1 if node.title.startswith('Chapter') else 0
    count += count_chapters(node.left)
    count += count_chapters(node.right)
    return count

def find_topics_containing_words(node, words):
    if node is None:
        return
    if all(word.lower() in node.title.lower() for word in words):
        print(node.title, node.page)
    find_topics_containing_words(node.left, words)
    find_topics_containing_words(node.right, words)

# Cargar el índice desde un archivo de texto
index = load_index_from_file('/ruta/completa/para/indice.txt')

# Construir el árbol binario no balanceado usando la transformada de Knuth
root = build_knuth_transform(index)

# Listar el índice en su orden original
print("Índice en su orden original:")
for title, page in index:
    print(f"{title}: Página {page}")

print("\nParte del índice correspondiente al subtítulo 'Diseño de software de tiempo real':")
find_subtitle(root, "Diseño de software de tiempo real")

print("\nNúmero de capítulos:", count_chapters(root))

print("\nTemas que contienen las palabras 'modelo' y 'métrica':")
find_topics_containing_words(root, ["modelo", "métrica"])