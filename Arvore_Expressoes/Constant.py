class Constant():

    def __init__(self, cons):
        self.cons = cons

    def val(self):
        return int(self.cons)

    def __str__(self):
        return str(self.cons)

