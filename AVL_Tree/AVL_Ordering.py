class node:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        #Returns list of strings, width, height, and horizontal coordinate of the root.
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


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
        
    def insert(self, word_val, root):
        if root is None:
            return node(word_val)
        # Then if VALUE is less than [root value], check if the value at left of root is less than VALUE
        elif (root.value > word_val or word_val == root.value):
            root.left = self.insert(word_val, root.left)
        # Then if VALUE is greater than [root value], check if the value at right of root is greater than VALUE
        else:
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

    def preorder(self, root):
            if root is None:
                return
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

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
    with open(path_file, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                counter += 1
    return counter

def return_word(path, index):
    f = open(path, encoding='utf-8')
    seperate = list(f.read().lower().split('\n'))
    seperate = list(filter(None, seperate))
    seperate = [words for segments in seperate for words in segments.split()]
    f.close()
    return seperate[index-1].strip()

def search(root, key):
    if root is None:
        return 'Not found'
    elif root.value == key:
        print()
        print('Word found: ')
        return root.value

    # Value is greater than root's key
    if root.value < key:
        return search(root.right, key)

    # Value is smaller than root's key
    return search(root.left, key)

def menu():
    option = None
    Tree = None
    rt = None
    pathFile = ''

    while(option != 0):
        print('Choose one option: ')
        print('1 - Load default file')
        print('2 - Load custom file with path')
        print('3 - Print the AVL tree')
        print('4 - Search word in tree')
        print('0 - To end the program')

        option = input()      
        
        if (option == '1'):     
            Tree = AVL()
            rt = None
            pathFile = 'words.txt'
            print('\n[', pathFile, '] file loaded\n')
            counter = count_words_file(pathFile)
            i = 0
            while (i < counter):
                rt = Tree.insert(return_word(pathFile, i), rt)
                i += 1
        elif option == '2':
            Tree = AVL()
            rt = None
            print('Input file path: ')
            pathFile = input()
            pathFile = pathFile.lower()
            print('\n[', pathFile, '] file loaded\n')
            counter = count_words_file(pathFile)
            i = 0
            while (i < counter):
                rt = Tree.insert(return_word(pathFile, i), rt)
                i += 1
        elif (option == '3'):
            if Tree == None:
                print('Tree not created yet')
            else:
                rt.display()
        elif (option == '4'):
            if Tree == None:
                print('Tree not created yet')
            else:
                print('Insert word to be searched: ')
                word = input()
                print(search(rt, word))
        elif option == '0':
            break
   
menu()
