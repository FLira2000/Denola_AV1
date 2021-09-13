class Member:
    def __init__(self, name, mother = None, father = None):
        self.name = name
        self.mother = mother
        self.father = father

    def __str__(self):
        return self.name    

    def get_parents(self):
        return (self.mother, self.father)
