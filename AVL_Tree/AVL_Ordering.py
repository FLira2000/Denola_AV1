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

    def insert_word(self, word_val, root):
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


    #TODO: intersect value as calculation of words alphabetic order,
    # so, value is the value of alphabetic order of a word
    # maybe, check value inside function to see if it's higher than the node.value is being compared to
    def insert(self, val, root):
        if root is None:
            return node(val)
        # Then if VALUE is less than [root value], check if the value at left of root is less than VALUE
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        # Then if VALUE is greater than [root value], check if the value at right of root is greater than VALUE
        elif val > root.value:
            root.right = self.insert(val, root.right)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        
        # if balance is less than -1 and greater than 1, it needs to be balanced
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    # prints the tree as far as I noticed
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

    # TODO: needs work
    def tree_search(self, word):
        if self.root is None:
            return node(val)
        # Then if VALUE is less than [root value], check if the value at left of root is less than VALUE
        elif val <= root.value:
            root.left = self.tree_search(val, root.left)
        # Then if VALUE is greater than [root value], check if the value at right of root is greater than VALUE
        elif val > root.value:
            root.right = self.tree_search(val, root.right)


def test_normal():
    Tree = AVL()
    rt = None
    rt = Tree.insert(1, rt)
    rt = Tree.insert(2, rt)
    rt = Tree.insert(3, rt)
    rt = Tree.insert(4, rt)
    rt = Tree.insert(5, rt)
    print("PREORDER")
    Tree.preorder(rt)

def test_word():
    Tree = AVL()
    rt = None
    rt = Tree.insert_word('azul', rt)
    rt = Tree.insert_word('amarelo', rt)
    rt = Tree.insert_word('verde', rt)
    rt = Tree.insert_word('viril', rt)
    rt = Tree.insert_word('anao', rt)
    rt = Tree.insert_word('vizil', rt)
    print("PREORDER")
    Tree.preorder(rt)

test_word()
print(' aein ')
test_normal()