from ExpressionParser import infixToPost
from Operator import Operator
from Constant import Constant

class Expression_Tree:
    root = None
    level = 0

    def __init__(self, exp: str):
        splited = list(filter(lambda e: e != '', infixToPost(exp).split('|')))
        self.create_tree(splited)

    def create_tree(self, lst):
        temp = None
        for elm in lst:
            if elm in  ['+', '-', '/', '*']:
                if temp == None:
                    tmp = Operator(elm)
                    continue
                elif temp
                
