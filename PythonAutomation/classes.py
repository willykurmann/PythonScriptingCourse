class A:
    d = 100

    def __init__(self):
        print("This is constructor")

    def display(self):
        print("This is display method")

    def sum(self,a,b):
        print(a+b)
    
    def classvar(self):
        print("this is class variable d: {}".format(A.d))

a = A()
a.display()
a.sum(1,2)
a.classvar()
