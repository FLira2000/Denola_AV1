class Operator():
    def __init__(self, op, l = None, r = None):
        
        if op not in ['+','-','/','*']:
            raise Exception(f"Invalid operation selected for Operator. '{op}' not supported. ")

        self.op = op
        self.l = l
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
        
