class node:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    def balance(self, Node):
        if Node is None:
            return 0
        else:
            return self.height(Node.left) - self.height(Node.right)

    def MinimumValueNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else:
            return self.MinimumValueNode(Node.left)

    def rotateR(self, Node):
        a = Node.left
        b = a.right
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotateL(self, Node):
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def check_words(self, word1, word2):
        i = 0
        j = 0
        if(len(word1) > len(word2)):
            i = len(word2)
        else:
            i = len(word1)

        while(j < i):
            if(word1[j] > word2[j]):
                return True
            j += 1
        return False

    def insert(self, word_val, root):
        if root is None:
            return node(word_val)
        # Then if VALUE is less than [root value], check if the value at left of root is less than VALUE
        elif (self.check_words(root.value, word_val)):
            root.left = self.insert(word_val, root.left)
        # Then if VALUE is greater than [root value], check if the value at right of root is greater than VALUE
        elif (word_val, root.value):
            root.right = self.insert(word_val, root.right)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        
        # if balance is less than -1 and greater than 1, it needs to be balanced
        if balance > 1 and root.left.value > word_val:
            return self.rotateR(root)
        if balance < -1 and word_val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and word_val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and word_val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.value:
            Node.left = self.delete(val, Node.left)
        elif val > Node.value:
            Node.right = self.delete(val, Node.right)
        else:
            if Node.left is None:
                lt = Node.right
                Node = None
                return lt
            elif Node.right is None:
                lt = Node.left
                Node = None
                return lt
            rgt = self.MinimumValueNode(Node.right)
            Node.value = rgt.value
            Node.right = self.delete(rgt.value, Node.right)
        if Node is None:
            return Node

        # Re-do balacing the tree
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        balance = self.balance(Node)
        if balance > 1 and self.balance(Node.left) >= 0:
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) <= 0:
            return self.rotateL(Node)
        if balance > 1 and self.balance(Node.left) < 0:
            Node.left = self.rotateL(Node.left)
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) > 0:
            Node.right = self.rotateR(Node.right)
            return self.rotateL(Node)
        return Node

def print_tree(node, level=0):
    if node != None:
        print_tree(node.left, level + 1)
        print(' ' * 6 * level + '->', node.value)
        print_tree(node.right, level + 1)

def count_words_file(path_file):
    counter = 0
    with open(path_file,'r') as f:
        for line in f:
            for word in line.split():
                counter +=1
    return counter


def search(root,key):
    if root is None:
        return 'Not found' 
    elif root.value == key:
        return root.value
 
    # Value is greater than root's key
    if root.value < key:
        return search(root.right,key)
   
    # Value is smaller than root's key
    return search(root.left,key)        


def return_word(path, index):
    f = open(path)
    seperate = list(f.read().split(" "))
    f.close()
    return seperate[index]

pathWord = 'C:/Users/usr1/Desktop/words.txt'

Tree = AVL()
rt = None
counter = count_words_file(pathWord)
i = 0
while(i < counter):
    print(return_word(pathWord, i))
    rt = Tree.insert(return_word(pathWord, i), rt)
    i += 1
print_tree(rt)

word_search = 'fonfon'
print('Searching word: ', word_search)
print('   ', search(rt, word_search))
