import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_freq = node1.freq + node2.freq
        merged_node = HuffmanNode(None, merged_freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_freq_table(message):
    freq_table = defaultdict(int)
    for char in message:
        freq_table[char] += 1
    return freq_table

def build_encoding_table(huffman_tree):
    encoding_table = {}
    def traverse(node, code):
        if node.char:
            encoding_table[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    traverse(huffman_tree, '')
    return encoding_table

def compress(message, encoding_table):
    compressed_message = ''
    for char in message:
        compressed_message += encoding_table[char]
    return compressed_message

def decompress(compressed_message, huffman_tree):
    decompressed_message = ''
    current_node = huffman_tree
    for bit in compressed_message:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char:
            decompressed_message += current_node.char
            current_node = huffman_tree
    return decompressed_message

# Ejemplo de uso
message = "Hola, soy Poe Dameron"
freq_table = build_freq_table(message)
huffman_tree = build_huffman_tree(freq_table)
encoding_table = build_encoding_table(huffman_tree)
compressed_message = compress(message, encoding_table)
decompressed_message = decompress(compressed_message, huffman_tree)

print("Mensaje original:", message)
print("Mensaje comprimido:", compressed_message)
print("Mensaje descomprimido:", decompressed_message)