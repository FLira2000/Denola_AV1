import Element

class Operator(Element):
    def __init__(self, op, l, r):
        
        if op not in ['+','-','/','*']:
            raise Exception(f"Invalid operation selected for Operator. '{op}' not supported. ")

        self.op = op
        self.l = l
        self.r = r

    def eval():
        cases = {
            '/': self.l.eval() / self.r.eval(),
            '*': self.l.eval() * self.r.eval(),
            '+': self.l.eval() + self.r.eval(),
            '-': self.l.eval() - self.r.eval()
        }

        return cases[op]
        
