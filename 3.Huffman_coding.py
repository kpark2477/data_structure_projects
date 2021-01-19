import sys

class Node(object):
        
    def __init__(self, size: int, char: str = None):
        self.size = size
        self.char = char
        self.left = None
        self.right = None
        
    def set_size(self, size):
        self.size = size
        
    def set_char(self, char):
        self.char = char
    
    def get_size(self):
        return self.size
    
    def get_char(self):
        return self.char
    
    def set_left_child(self, left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def is_leaf_node(self):
        return self.left == None and self.right == None

    def __repr__(self):
        return f"Node(char {self.get_char()}, size {self.get_size()})"


class Tree(object):

    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root


def huffman_encoding(data):

    char_freq = {}
    arry = []
    for i in data: 
        if i in char_freq: 
            char_freq[i] += 1
        else: 
            char_freq[i] = 1
    
    for key in char_freq:
        arry.append(Node(char_freq[key], key))
    
    def remove_the_smallest_node(arry):
        index = -1
        smallest_node = arry[0]
        for i in arry:
            index += 1
            if i.get_size() <= smallest_node.get_size():
                smallest_node = i
                smallest_node_index = index
        arry.pop(smallest_node_index)
        return smallest_node
    
    while len(arry) >= 2:
        small1 = remove_the_smallest_node(arry)
        small2 = remove_the_smallest_node(arry)
        new_node = Node(small1.get_size()+small2.get_size())
        new_node.set_left_child(small1)
        new_node.set_right_child(small2)
        arry.append(new_node)

    if arry[0].is_leaf_node:
        # when input string only consists of one character
        new_node = Node(1) # Size of node doesn't matter, in this case 1 is chosen.
        new_node.set_left_child(arry[0])
        tree = Tree(new_node)
    else:
        tree = Tree(arry[0])

    encoding_dict = {}
    huff_code_tracking = list()

    def tree_traverse(node):
        if node:
            if node.is_leaf_node():
                code = ''
                for i in huff_code_tracking:
                    code += str(i)
                encoding_dict[node.get_char()] = code
                pass
            huff_code_tracking.append(0)
            tree_traverse(node.left)
            huff_code_tracking.append(1)
            tree_traverse(node.right)
            if len(huff_code_tracking) != 0:
                huff_code_tracking.pop()
        else:
            huff_code_tracking.pop()
    
    tree_traverse(tree.get_root())

    encoded_data = ''

    for i in data:
        encoded_data += encoding_dict[i]

    return encoded_data, tree


def huffman_decoding(data,tree):
    current_node = tree.get_root()
    decoded_data = ''
    for i in data:
        if i == '0':
            current_node = current_node.left
            if current_node.is_leaf_node():
                decoded_data += current_node.get_char()
                current_node = tree.get_root()
        else:
            current_node = current_node.right
            if current_node.is_leaf_node():
                decoded_data += current_node.get_char()
                current_node = tree.get_root() 

    return decoded_data



### test cases

def test(input_string):

    print ("The size of the data is: {}".format(sys.getsizeof(input_string)))
    print ("The content of the data is: {}".format(input_string))

    encoded_data, tree = huffman_encoding(input_string)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}".format(decoded_data))
    print ("\n")


test('I hate covid') # normal case
test('aaaaaa') # an edge case which only consists of one character.
test('abcdefghijklmnopqrstuvwxyz') # an edge case where all letter are different characters.
