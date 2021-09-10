from Leaf import Leaf

class GenTree:
    root: None

    def performInsertion(self, child: Leaf, parent: Leaf, pos):
        if pos == 1:
            child.mother = parent
        elif pos == 2:
            child.father = parent
    
    def searchLeaf(self, leafId) -> Leaf:
        pass

    def searchLeaf(self, childName) -> Leaf:
        pass

    def insertLeaf(self, parentLeaf, childLeafId = None, whichParent = 0):
        if childLeafId != None:
            self.performInsertion(child = self.searchLeaf(childLeafId), parent=parentLeaf, whichParent=whichParent)
            return
        else:
            self.root = parentLeaf
    
    def insertLeaf(self, parentLeaf, childLeafName = None, whichParent = 0):
        if childLeafName != None:
            self.performInsertion(child = self.searchLeaf(childLeafName), parent=parentLeaf, whichParent=whichParent)
            return
        else:
            self.root = parentLeaf
    
    def printTree(self, root = None):
        if root == None:
            self.root.printMyself()
            if self.root.mother != None: 
                self.printTree(self.root.mother)
        
            if self.root.father != None: 
                self.printTree(self.root.father)
        else:
            root.printMyself()
            if root.mother != None: 
               self.printTree(root.mother)
        
            if root.father != None: 
                self.printTree(root.father)
                
