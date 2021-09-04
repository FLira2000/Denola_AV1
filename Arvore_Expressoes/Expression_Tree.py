from ExpressionParser import infixToPost
from Operator import Operator
from Constant import Constant

class Expression_Tree:
    root = None
    level = 0

    def __init__(self, exp: str):
        self.exp = exp
        splited = list(filter(lambda e: e != '', infixToPost(exp).split('|')))
        print(splited)
        self.create_tree(splited)

    def create_tree(self, lst):
        l, r, op = lst[0], lst[1], lst[2]
        print(op, l, r)
        self.root = Operator(op, l, r)
        root+=1

    def eval(self):
        if root == None:
            return None
        else:
            return self.root.val()
