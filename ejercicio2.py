class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(TreeNode(int(char)))
        else:
            node = TreeNode(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

def evaluate_expression_tree(node):
    if node.value.isdigit():
        return int(node.value)
    left_result = evaluate_expression_tree(node.left)
    right_result = evaluate_expression_tree(node.right)
    if node.value == '+':
        return left_result + right_result
    elif node.value == '-':
        return left_result - right_result
    elif node.value == '*':
        return left_result * right_result
    elif node.value == '/':
        return left_result / right_result

# Ejemplo de uso
expression = "52+3*"
root = build_expression_tree(expression)
print("Expresión en orden correcto (inorder traversal):")
inorder_traversal(root)
print("\nResultado de la expresión matemática:", evaluate_expression_tree(root))