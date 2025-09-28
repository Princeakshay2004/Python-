# Multilevel Inheritance


class A:
    def readA(self):
        print("Hello A")


class B(A):
    def readB(self):
        print("Hello B")



class C(B):
    def readC(self):
        print("Hello C")


obj=C()
obj.readA()
obj.readB()
obj.readC()