class Member:
    def __init__(self, name):
        self.name = name
        self.mother = None
        self.father = None

    def __str__(self):
        return self.name    

    def add_parents(self, mother, father):
        self.mother = mother
        self.father = father

    def get_parents(self):
        return (self.mother, self.father)
