import heapq

class Node:
    def __init__(self, count, children):
        self.count    = count
        self.children = children
        
    def is_leaf(self):
        return False
        
    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count
        
class LeafNode(Node):
    def __init__(self, symbol, count):
        super().__init__(count, [])
        self.symbol = symbol
        
    def is_leaf(self):
        return True

class HuffmanCode:
    def __init__(self, F):
        self.C = dict()
        self.T = None
        self.cost = 0
        self.average_cost = 0
        self.F = F
        self.LeafNode_list = []
        for key, value in F.items():
            self.LeafNode_list.append(LeafNode(key, value))
        heapq.heapify(self.LeafNode_list)
        while len(self.LeafNode_list) > 1:
            node1 = heapq.heappop(self.LeafNode_list)
            node2 = heapq.heappop(self.LeafNode_list)
            childrenList = [node1, node2]
            newNode = Node(node1.count + node2.count, childrenList)
            heapq.heappush(self.LeafNode_list, newNode)

        self.T = heapq.heappop(self.LeafNode_list)
        binary_code = ""

        self.dfs_helper(self.T, binary_code)
    
    def dfs_helper(self, node, binary_code):
        if node.is_leaf() == True:
            self.C[node.symbol] = binary_code
        else:
            self.dfs_helper(node.children[0], binary_code + '0')
            self.dfs_helper(node.children[1], binary_code + '1')

    def encode(self, m):
        """
        Uses self.C to encode a binary message.
.    
        Parameters:
            m: A plaintext message.
        
        Returns:
            The binary encoding of the plaintext message obtained using self.C.
        """
        
        binaryCode = ''
        for c in range (len(m)):
            binaryCode = binaryCode + self.C[m[c]]
        return binaryCode

    def decode(self, c):
        """
        Uses self.T to decode a binary message c = encode(m).
.    
        Parameters:
            c: A message encoded in binary using self.encode.
        
        Returns:
            The original plaintext message m decoded using self.T.
        """
        
        message = ''
        node = self.T
        for s in c:
            if (s == '0'):
                node = node.children[0]
                if node.is_leaf() == True:
                    message = message + node.symbol
                    node = self.T
            else:
                node = node.children[1]
                if node.is_leaf() == True:
                    message = message + node.symbol
                    node = self.T
        return message

        
    def get_cost(self):
        """
        Returns the cost of the Huffman code as defined in CLRS Equation 16.4.
        
        Returns:
            Returns the cost of the Huffman code.
        """ 
        for symbol in self.F:
            self.cost = self.cost + (len(self.C[symbol]) * self.F[symbol])

        return self.cost
        
def get_frequencies(s):
    """
    Computes a frequency table for the input string "s".
    
    Parameters:
        s: A string.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in s).
    """

    F = dict()
    
    for char in s:
        if not(char in F):
            F[char] = 1
        else:
            F[char] += 1
            
    return F
    
def get_frequencies_from_file(file_name):
    """
    Computes a frequency table from the text in file_name.
    
    Parameters:
        file_name: The name of a text file.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in the contents of <file_name>).
    """
    f = open(file_name, "r")
    s = f.read()
    f.close()

    return get_frequencies(s)

HuffmanCode1 = HuffmanCode(get_frequencies_from_file('/Users/yangcan/Documents/CS325/assignment3/cs325-w23-homework3-gettysburg-address.txt'))
print(HuffmanCode1.encode('hello world'))
print(HuffmanCode1.decode(HuffmanCode1.encode('hello world I love you')))
print(HuffmanCode1.get_cost())