
# Hierarchical Inheritance

class A:
    def __init__(self):
        print("Welcome Everyone")
    
    def readA(Self):
        print("Hello A")


class B(A):
    def readB(self):
        print("Hello B")
    
class C(A):
    def readC(self):
        print("Hello C")



obj=B()
obj.readA()
obj.readB()


obj1=C()
obj1.readA()
obj1.readC()