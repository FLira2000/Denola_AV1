from Constant import Constant

class Operator():
    def __init__(self, op = None, l = None, r = None):
        
        if op not in ['+','-','/','*', None]:
            raise Exception(f"Invalid operation selected for Operator. '{op}' not supported. ")
        self.op = op

        if l in ['+','-','/','*']:
            self.l = Operator(l)
        else:
            self.l = l

        if r in ['+','-','/','*']:
            self.r = Operator(r)
        else:
            self.r = r

    def val(self):
        if self.l == None or self.r == None:
            raise Exception('No operands to perform the operation.')
        
        cases = {
            '/': self.l.val() / self.r.val(),
            '*': self.l.val() * self.r.val(),
            '+': self.l.val() + self.r.val(),
            '-': self.l.val() - self.r.val()
        }

        return cases[self.op]
