from ExpressionParser import infixToPostList
from Operator import Operator
from Constant import Constant

class ExpressionTree:
    root: Operator = None
    exp: str = None

    def __init__(self, exp: str):
        self.exp = exp
        self.create_tree(infixToPostList(exp))

    def isOperator(self, el):
        if el in ['-', '+', '*', '/']:
            return True
        else:
            return False

    def create_tree(self, postexp):
        stack = []

        for el in postexp:
            if not self.isOperator(el):
                stack.append(Constant(el))
            else:
                e1, e2 = stack.pop(), stack.pop()
                stack.append( Operator(el, e1, e2) )

        self.root = stack.pop()
        
    def eval(self):
        if self.root == None:
            return None
        else:
            return self.root.val()

    def print_tree(self, elm, lvl=0):            

        if type(elm) == Constant:
            print('   ' * lvl + '> ' + str(elm))
        elif type(elm) == Operator:
            self.print_tree(elm.l, lvl=lvl + 1)
            print('   ' * lvl + '> ' + str(elm))
            self.print_tree(elm.r, lvl=lvl + 1)
        else:
            return
   
    def print(self):
        self.print_tree(self.root)
