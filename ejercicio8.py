class Node:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []

def inorder_traversal(node):
    if node:
        inorder_traversal(node.children[0])
        print(node.name)
        inorder_traversal(node.children[1])
        
def list_files_in_directory(node, directory):
    if node.name == directory:
        for child in node.children:
            if not child.is_directory:
                print(child.name)
    else:
        for child in node.children:
            list_files_in_directory(child, directory)

def count_files_in_directory(node, directory):
    count = 0
    if node.name == directory:
        for child in node.children:
            if not child.is_directory:
                count += 1
    else:
        for child in node.children:
            count += count_files_in_directory(child, directory)
    return count

def get_min_node(node):
    if not node.children:
        return node
    return get_min_node(node.children[0])

def get_max_node(node):
    if not node.children:
        return node
    return get_max_node(node.children[-1])

# Example usage
root = Node("/")
images = Node("Imágenes", is_directory=True)
root.children.append(images)
images.children.append(Node("image1.jpg"))
images.children.append(Node("image2.jpg"))
images.children.append(Node("image3.jpg"))
documents = Node("Documentos", is_directory=True)
root.children.append(documents)
documents.children.append(Node("document1.pdf"))
documents.children.append(Node("document2.pdf"))

# Transforming to a binary tree using Knuth's transform
def knuth_transform(node):
    if len(node.children) > 2:
        new_node = Node(node.name, node.is_directory)
        new_node.children.append(node.children[0])
        for child in node.children[1:]:
            new_node.children.append(knuth_transform(child))
        return new_node
    else:
        return node

binary_tree_root = knuth_transform(root)

# Inorder traversal
print("Inorder traversal:")
inorder_traversal(binary_tree_root)

# List files in /Imágenes directory
print("Files in /Imágenes directory:")
list_files_in_directory(binary_tree_root, "Imágenes")

# Count files in each directory
print("Number of files in each directory:")
print("Files in /Imágenes:", count_files_in_directory(binary_tree_root, "Imágenes"))
print("Files in /Documentos:", count_files_in_directory(binary_tree_root, "Documentos"))

# Get minimum and maximum nodes
print("Minimum node:", get_min_node(binary_tree_root).name)
print("Maximum node:", get_max_node(binary_tree_root).name)