class Formula:
    def __init__(self,subformulas):
        self.subformulas  = subformulas
    def subf(self):
        return self.subformulas
    def toString(self):
        return ""
    def eval(self,i):
        return False

class Variable(Formula):
    def __init__(self,name):
        Formula.__init__(self,[]) #premenna nema podformuly
        self.name = name

    def toString(self):
        return self.name

    def eval(self,i):
        return  i[self.name] #pozrie do slovnika ci je premenna true / false

    
class Negation(Formula):
    def __init__(self,formula):
        Formula.__init__(self,[formula])

    def originalFormula(self):
        return self.subf()[0]

    def toString(self):
        return "-" + self.originalFormula().toString()

    def eval(self,i):
        return not self.originalFormula().eval(i)

class Conjunction(Formula):
    def __init__(self,subformulas):
        Formula.__init__(self,subformulas)

    def toString(self):
        s = "("
        spoj = ""
        for sf in self.subf():
            s+= spoj
            s+= sf.toString()
            spoj = "&"
        s+= ")"
        return s
    
    def eval(self, i):
        for sf in self.subf():
            if sf.eval(i) == False:
                return False
        return True
    # eval ak vsetky vratia true tak vrati true ...
    
class Disjunction(Formula):
    def __init__(self,subformulas):
        Formula.__init__(self,subformulas)
        
    def toString(self):
        s = "("
        spoj = ""
        for sf in self.subf():
            s+= spoj
            s+= sf.toString()
            spoj = "|"
        s+= ")"
        return s
    
    def eval(self,i):
        for sf in self.subf():
            if sf.eval(i):
                return True #aspon jedna true
        return False

class BinaryFormula(Formula):
    def __init__(self,left,right):
        self.left = left
        self.right = right
        
    def leftSide(self):
        return self.left
    
    def rightSide(self):
        return self.right

    def eval(self,i):
        pass

    def toString(self):
        pass
    
class Implication(BinaryFormula):
    def __init__(self,left,right):
        self.left = left
        self.right = right
        BinaryFormula.__init__(self,left,right)
    
    def toString(self):
        return "({}=>{})".format(self.left.toString(),self.right.toString())

    def eval(self,i):
        return not self.leftSide().eval(i) or self.rightSide().eval(i)
    
        

class Equivalence(BinaryFormula):
    def __init__(self,left,right):
        self.left = left
        self.right = right
        BinaryFormula.__init__(self,left,right)
    
    def toString(self):
        return "({}<=>{})".format(self.left.toString(),self.right.toString())
        
    def eval(self,i):
        return (self.leftSide().eval(i) == self.rightSide().eval(i))      
