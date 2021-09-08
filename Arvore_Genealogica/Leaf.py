from random import random

class Leaf:
    def __init__(self, founder):
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        self.parent = mother   

    def get_parent(self):
        return self.parent 

    def is_parent(self, mother):
        return self.parent == mother  

    def add_child(self, child):
        self.children.append(child)   

    def is_child(self, child):
        return child in self.children 
