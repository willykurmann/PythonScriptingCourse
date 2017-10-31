class A:
    def __init__(self):
        print("this is A constructor")
    
    def methA(self):
        print("this is method A")
    
    def methZ(self):
        print("this is method Z from class A")

class B(A):
    def __init__(self):
        print("this is B constructor")
    
    def methB(self):
        print("this is method B")

class Z(B):
    def __init__(self):
        B.__init__(self)
        print("this is Z constructor")
    
    def methZ(self):
        print("this is method Z from class Z") 

ob = B()
ob.methA()
ob.methB()
ob.methZ()

ob2 = Z()
ob2.methA()
ob2.methB()
ob2.methZ()