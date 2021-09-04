from typings import List

class Expression_Tree:
    root = None
    level = 0
    _parser = lambda exp: list(filter(lambda e: e != '', exp.split('|')))

    def __init__(self, exp: str):
        exp = self._parser(exp)
        #self.insert_element

    def insert_element(self, op, elm):
        pass
